from abc import ABC, abstractmethod
from models import PurchasedLottery


class PurchasedLotteryRepository(ABC):
    @abstractmethod
    def find_purchased_lottery(self) -> PurchasedLottery:
        ...

    @abstractmethod
    def find_all_purchased_lotteries(self) -> list[PurchasedLottery]:
        ...

    @abstractmethod
    def save_purchased_lottery(self, purchased_lottery: PurchasedLottery) -> None:
        ...


class PurchasedLotteryRepositoryV0(PurchasedLotteryRepository):
    def find_purchased_lottery(self) -> PurchasedLottery:
        pass

    def find_all_purchased_lotteries(self) -> list[PurchasedLottery]:
        pass

    def save_purchased_lottery(self, purchased_lottery: PurchasedLottery) -> None:
        pass
