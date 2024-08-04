from abc import ABC, abstractmethod

from models import Lottery
from repositories.base_repository import BaseRepository
import ast


class LotteryRepository(ABC, BaseRepository):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def find_lottery_by_round_number(self, round_number: int) -> Lottery:
        ...

    @abstractmethod
    def find_all_lottery(self) -> list[Lottery]:
        ...

    @abstractmethod
    def save_lottery(self, lottery: Lottery) -> None:
        ...


class LotteryRepositoryV0(LotteryRepository):
    def __init__(self):
        super().__init__()

    def find_lottery_by_round_number(self, round_number: int) -> Lottery:
        select_query = """
        select round_number, draw_date, winning_numbers, bonus_number from lottery
        where round_number = %s
        """
        params = (round_number,)

        results = self.db_manager.execute_query(
            query=select_query,
            params=params
        )

        return Lottery(
                round_number=int(results[0].get("round_number")),
                draw_date=str(results[0].get("draw_date")),
                winning_numbers=ast.literal_eval(results[0].get("winning_numbers")),
                bonus_number=int(results[0].get("bonus_number"))
            )

    def find_all_lottery(self) -> list[Lottery]:
        select_query = """
        select round_number, draw_date, winning_numbers, bonus_number from lottery
        """

        results = self.db_manager.execute_query(
            query=select_query
        )

        return [
            Lottery(
                round_number=int(result.get("round_number")),
                draw_date=str(result.get("draw_date")),
                winning_numbers=ast.literal_eval(result.get("winning_numbers")),
                bonus_number=int(result.get("bonus_number"))
            )
            for result in results
        ]

    def save_lottery(self, lottery: Lottery) -> None:
        insert_query = """
        insert into lottery (round_number, draw_date, winning_numbers, bonus_number)
        values (%s, %s, %s, %s)
        """

        params = (lottery.round_number, lottery.draw_date, lottery.winning_numbers_str, lottery.bonus_number)

        self.db_manager.insert_data(
            query=insert_query,
            params=params
        )

