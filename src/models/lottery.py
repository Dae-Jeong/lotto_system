from utils import calculate_round_number
from datetime import date


class Lottery:
    def __init__(self,
                 round_number: int,
                 draw_date: str,
                 winning_numbers: list[int],
                 bonus_number: int):
        self.__round_number = round_number
        self.__draw_date = draw_date
        self.__winning_numbers = winning_numbers
        self.__bonus_number = bonus_number

    @property
    def round_number(self):
        return self.__round_number

    @property
    def draw_date(self):
        return self.__draw_date

    @property
    def winning_numbers(self):
        return self.__winning_numbers

    @property
    def bonus_number(self):
        return self.__bonus_number


class PurchasedLottery:
    def __init__(self,
                 winning_numbers,
                 bonus_number):

        today = date.today().strftime("YYYY-mm-dd")
        super().__init__(round_number=calculate_round_number(today=today),
                         winning_numbers=winning_numbers,
                         bonus_number=bonus_number)

