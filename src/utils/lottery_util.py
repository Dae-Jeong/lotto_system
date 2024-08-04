from datetime import date
from random import sample
from consts import LOTTERY_MIN_NUMBER, LOTTERY_MAX_NUMBER, LOTTERY_COUNT, LOTTERY_FIRST_DATE, LOTTERY_URL


def get_lottery_page_url(page_number: int):
    return f"{LOTTERY_URL}?page={str(page_number)}"


def get_lottery_number_from_img_src(img_src: str):
    """
    이미지 소스 경로
    https://www.lotto.co.kr/resources/images/lottoball_92/on/{당첨번호}.png

    :param img_src:
    :return:
    """
    return int(img_src.split("/")[-1].split(".")[0])


def generate_lottery_numbers() -> tuple[list[int], int]:
    generated_numbers = sample(range(LOTTERY_MIN_NUMBER, LOTTERY_MAX_NUMBER+1), LOTTERY_COUNT)
    return sorted(generated_numbers[:-1]), generated_numbers[-1]


def calculate_round_number(today: str):
    today_dt = date.fromisoformat(today)
    first_day_dt = date.fromisoformat(LOTTERY_FIRST_DATE)
    diff = today_dt - first_day_dt

    return (diff.days // 7) + 1
