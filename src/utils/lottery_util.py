from datetime import date
from random import sample
from models import Lottery
from models.enums import LottoResult
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
    return img_src.split("/")[-1].split(".")[0]


def generate_lottery_numbers() -> tuple[list[int], int]:
    generated_numbers = sample(range(LOTTERY_MIN_NUMBER, LOTTERY_MAX_NUMBER+1), LOTTERY_COUNT)
    return sorted(generated_numbers[:-1]), generated_numbers[-1]


def calculate_round_number(today: str):
    today_dt = date.fromisoformat(today)
    first_day_dt = date.fromisoformat(LOTTERY_FIRST_DATE)
    diff = today_dt - first_day_dt

    return (diff.days // 7) + 1


def check_lotto_result(user_lottery: Lottery, winning_lottery: Lottery) -> LottoResult:
    match_count = __check_match_number_count(
        user_numbers=user_lottery.winning_numbers,
        winning_numbers=winning_lottery.winning_numbers
    )

    is_bonus_number_match = __check_bonus_number_match(
        user_bonus_number=user_lottery.bonus_number,
        winning_bonus_number=winning_lottery.bonus_number
    )

    if match_count == 6:
        return LottoResult.FIRST
    elif match_count == 5 and is_bonus_number_match:
        return LottoResult.SECOND
    elif match_count == 5:
        return LottoResult.THIRD
    elif match_count == 4:
        return LottoResult.FOURTH
    elif match_count == 3:
        return LottoResult.FIFTH
    else:
        return LottoResult.NONE


def __check_bonus_number_match(user_bonus_number, winning_bonus_number):
    is_bonus_number_match = user_bonus_number == winning_bonus_number
    return is_bonus_number_match


def __check_match_number_count(user_numbers, winning_numbers):
    match_count = len(set(user_numbers) & set(winning_numbers))
    return match_count
