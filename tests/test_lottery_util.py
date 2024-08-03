from utils.lottery_util import *
from models import Lottery
import pytest
import datetime

@pytest.fixture
def sample_user_lotto_data():
    return Lottery(
        round_number=1000,
        draw_date='2023-01-01',
        winning_numbers=[1, 2, 3, 4, 5, 6],
        bonus_number=7
    )


@pytest.fixture
def sample_winning_lotto_data():
    return Lottery(
        round_number=1000,
        draw_date='2023-01-01',
        winning_numbers=[1, 2, 3, 4, 5, 6],
        bonus_number=7
    )


@pytest.fixture
def sample_today():
    return datetime.datetime(year=2023, month=7, day=12)


def test_generate_lottery_numbers():
    lottery_numbers, bonus_number = generate_lottery_numbers()
    assert len(lottery_numbers) == LOTTERY_COUNT - 1
    assert LOTTERY_MIN_NUMBER <= bonus_number <= LOTTERY_MAX_NUMBER


def test_check_lotto_result(sample_user_lotto_data, sample_winning_lotto_data):
    user_lottery = sample_user_lotto_data
    winning_lottery = sample_winning_lotto_data

    result = check_lotto_result(user_lottery=user_lottery, winning_lottery=winning_lottery)
    assert result.name == 'FIRST'


def test_calculate_round_number(sample_today):
    today = sample_today
    round_number = calculate_round_number()