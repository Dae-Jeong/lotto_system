from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from repositories import LotteryRepository
from utils import get_chrome_driver, get_lottery_page_url, get_lottery_number_from_img_src
from models import Lottery

from requests.exceptions import HTTPError
import requests
import time

"""
로또 결과 조회 페이지 : https://www.lotto.co.kr/article/list/AC01
페이지 이동 시 : https://www.lotto.co.kr/article/list/AC01?page={page_number}
"""


class CrawlerService(ABC):
    def __init__(self, lottery_repository: LotteryRepository):
        self.lottery_repository = lottery_repository
    
    @abstractmethod
    def crawl_winning_lottery(self):
        ...


class SeleniumCrawlerService(CrawlerService):
    def __init__(self, lottery_repository: LotteryRepository):
        super().__init__(lottery_repository=lottery_repository)
        self.driver = None
        self.by_dict = {
            "id": By.ID,
            "xpath": By.XPATH,
            "link text": By.LINK_TEXT,
            "partial link text": By.PARTIAL_LINK_TEXT,
            "name": By.NAME,
            "tag name": By.TAG_NAME,
            "class": By.CLASS_NAME,
            "css selector": By.CSS_SELECTOR
        }

    def get_driver(self) -> None:
        if not self.driver:
            self.driver = get_chrome_driver()

    def quit_driver(self) -> None:
        if self.driver:
            self.driver.quit()
            self.driver = None

    def get_elements(self, by: str, value: str, element: WebElement = None) -> list[WebElement]:
        kwargs = {"by": self.by_dict.get(by), "value": value}

        if element:
            return element.find_elements(**kwargs)
        return self.driver.find_elements(**kwargs)

    def get_element(self, by: str, value: str, element: WebElement = None) -> WebElement:
        kwargs = {"by": self.by_dict.get(by), "value": value}

        if element:
            return element.find_element(**kwargs)
        return self.driver.find_element(**kwargs)

    def get_parser(self, url: str):
        response = requests.get(url)
        response.raise_for_status()

        self.driver.get(url=url)

    def crawl_winning_lottery(self):
        self.get_driver()
        page_number = 1

        while True:
            page_url = get_lottery_page_url(page_number=page_number)

            try:
                self.get_parser(url=page_url)
            except HTTPError as http_error:
                print(http_error)  # 400, 500번대 오류 발생으로 인해 발생
                break

            time.sleep(1)  # 충분히 페이지가 로딩되길 기다리는 시간
            lottery_winning_ul_element = self.get_element(by="class", value="wnr_cur_list")
            lottery_winning_li_elements = self.get_elements(by="tag name",
                                                            value="li",
                                                            element=lottery_winning_ul_element)

            if not len(lottery_winning_li_elements):
                break

            for lottery_winning_li_element in lottery_winning_li_elements:
                winning_lottery = self.__get_winning_lottery(element=lottery_winning_li_element)
                self.__save_lottery(lottery=winning_lottery)

            page_number += 1
            time.sleep(2)  # 다음 요청까지의 시간 여유 확보

        self.quit_driver()

    def __get_winning_lottery(self, element: WebElement = None) -> Lottery:
        lottery_winning_span_elements = self.get_elements(by="tag name",
                                                          value="span",
                                                          element=element)

        round_number = int(lottery_winning_span_elements[0].text[:-1])
        draw_date = lottery_winning_span_elements[1].text
        winning_numbers, bonus_number = self.__get_winning_numbers_and_bonus_number(
            element=lottery_winning_span_elements[2]
        )

        return Lottery(
            round_number=round_number,
            draw_date=draw_date,
            winning_numbers=winning_numbers,
            bonus_number=bonus_number
        )

    def __get_winning_numbers_and_bonus_number(self, element: WebElement) -> tuple[list[int], int]:
        number_elements = self.get_elements(by="class", value="wball", element=element)
        numbers = []

        for number_element in number_elements:
            img_src = number_element.get_attribute('src')
            lottery_number = get_lottery_number_from_img_src(img_src=img_src)
            numbers.append(lottery_number)

        return numbers[:-1], numbers[-1]

    def __save_lottery(self, lottery: Lottery) -> None:
        self.lottery_repository.save_lottery(lottery=lottery)

