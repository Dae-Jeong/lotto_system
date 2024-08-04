from abc import ABC, abstractmethod

from models import Lottery
from databases import DBManager


class LotteryRepository(ABC):
    def __init__(self, db_manager: DBManager = DBManager()):
        self.db_manager = db_manager

    @abstractmethod
    def find_lottery_by_round_number(self, round_number: int):
        ...

    @abstractmethod
    def find_all_lottery(self):
        ...

    @abstractmethod
    def save_lottery(self, lottery: Lottery):
        ...


class LotteryRepositoryV0(LotteryRepository):
    def __init__(self):
        super().__init__()

    def find_lottery_by_round_number(self, round_number: int):
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
                round_number=results[0].get("round_number"),
                draw_date=results[0].get("draw_date"),
                winning_numbers=results[0].get("winning_numbers"),
                bonus_number=results[0].get("bonus_number")
            )

    def find_all_lottery(self):
        select_query = """
        select round_number, draw_date, winning_numbers, bonus_number from lottery
        """

        results = self.db_manager.execute_query(
            query=select_query
        )

        return [
            Lottery(
                round_number=result.get("round_number"),
                draw_date=result.get("draw_date"),
                winning_numbers=result.get("winning_numbers"),
                bonus_number=result.get("bonus_number")
            )
            for result in results
        ]

    def save_lottery(self, lottery: Lottery):
        insert_query = """
        insert into lottery (round_number, draw_date, winning_numbers, bonus_number)
        values (%s, %s, %s, %s)
        """

        params = (lottery.round_number, lottery.draw_date, lottery.winning_numbers, lottery.bonus_number)

        self.db_manager.insert_data(
            query=insert_query,
            params=params
        )

