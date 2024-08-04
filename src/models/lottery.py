from models.enums import LottoResult


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

    def __str__(self):
        winning_numbers_str = ', '.join(f"{num:02d}" for num in self.__winning_numbers)
        data = (f"{self.__round_number:<12}{self.__draw_date:<17}"
                f"{winning_numbers_str:<34}{self.__bonus_number:<15}")
        return data

    @property
    def round_number(self) -> int:
        return self.__round_number

    @property
    def draw_date(self) -> str:
        return self.__draw_date

    @property
    def winning_numbers_str(self) -> str:
        return str(self.__winning_numbers)

    @property
    def winning_numbers(self) -> list[int]:
        return self.__winning_numbers

    @property
    def bonus_number(self) -> int:
        return self.__bonus_number

    def check_lotto_result(self, user_winning_numbers: list[int], user_bonus_number: int) -> LottoResult:
        match_count = self.__check_match_number_count(
            user_numbers=user_winning_numbers
        )

        is_bonus_number_match = self.__check_bonus_number_match(
            user_bonus_number=user_bonus_number
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

    def __check_bonus_number_match(self, user_bonus_number) -> bool:
        is_bonus_number_match = user_bonus_number == self.bonus_number
        return is_bonus_number_match

    def __check_match_number_count(self, user_numbers) -> int:
        match_count = len(set(user_numbers) & set(self.winning_numbers))
        return match_count


class PurchasedLottery:
    def __init__(self,
                 purchased_lottery_id: str,
                 round_number: int,
                 winning_numbers: list[int],
                 bonus_number: int):

        self.__purchased_lottery_id = purchased_lottery_id
        self.__round_number = round_number
        self.__winning_numbers = winning_numbers
        self.__bonus_number = bonus_number

    @property
    def purchased_lottery_id(self) -> str:
        return self.__purchased_lottery_id

    @property
    def round_number(self) -> int:
        return self.__round_number

    @property
    def winning_numbers_str(self) -> str:
        return str(self.__winning_numbers)

    @property
    def winning_numbers(self) -> list[int]:
        return self.__winning_numbers

    @property
    def bonus_number(self) -> int:
        return self.__bonus_number
