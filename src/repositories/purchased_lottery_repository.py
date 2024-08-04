from abc import ABC, abstractmethod
from models import PurchasedLottery
from repositories.base_repository import BaseRepository


class PurchasedLotteryRepository(ABC, BaseRepository):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def find_purchased_lottery_by_id(self, purchased_lottery_id: str) -> PurchasedLottery:
        ...

    @abstractmethod
    def find_all_purchased_lotteries(self) -> list[PurchasedLottery]:
        ...

    @abstractmethod
    def save_purchased_lottery(self, purchased_lottery: PurchasedLottery) -> None:
        ...


class PurchasedLotteryRepositoryV0(PurchasedLotteryRepository):
    def find_purchased_lottery_by_id(self, purchased_lottery_id: str) -> PurchasedLottery:
        select_query = """
        select round_number, winning_numbers, bonus_number from purchased_lottery
        where purchased_lottery_id = %s
        """
        params = (purchased_lottery_id,)

        results = self.db_manager.execute_query(query=select_query, params=params)

        return PurchasedLottery(
            purchased_lottery_id=purchased_lottery_id,
            round_number=results[0].get("round_number"),
            winning_numbers=results[0].get("winning_numbers"),
            bonus_number=results[0].get("bonus_number")
        )

    def find_all_purchased_lotteries(self) -> list[PurchasedLottery]:
        select_query = """
        select purchased_lottery_id, round_number, winning_numbers, bonus_number from purchased_lottery
        """

        results = self.db_manager.execute_query(query=select_query)

        return [
            PurchasedLottery(
                purchased_lottery_id=result.get("purchased_lottery_id"),
                round_number=result.get("round_number"),
                winning_numbers=result.get("winning_numbers"),
                bonus_number=result.get("bonus_number")
            )
            for result in results
        ]

    def save_purchased_lottery(self, purchased_lottery: PurchasedLottery) -> None:
        print(purchased_lottery.purchased_lottery_id, purchased_lottery.round_number, purchased_lottery.winning_numbers_str, purchased_lottery.bonus_number)

        insert_query = """
        insert into purchased_lottery (purchased_lottery_id, round_number, winning_numbers, bonus_number)
        values (%s, %s, %s, %s)
        """

        params = (
            purchased_lottery.purchased_lottery_id,
            purchased_lottery.round_number,
            purchased_lottery.winning_numbers_str,
            purchased_lottery.bonus_number
        )

        self.db_manager.insert_data(query=insert_query, params=params)
