from abc import ABC, abstractmethod
from repositories import LotteryRepository, PurchasedLotteryRepository
from utils import generate_lottery_numbers
from models import PurchasedLottery


class LotteryService(ABC):
    def __init__(self,
                 lottery_repository: LotteryRepository,
                 purchased_lottery_repository: PurchasedLotteryRepository):
        self.lottery_repository = lottery_repository
        self.purchased_lottery_repository = purchased_lottery_repository

    @abstractmethod
    def purchase_lottery(self, purchase_mode: str):
        ...

    @abstractmethod
    def check_lottery(self):
        ...

    @abstractmethod
    def get_all_lottery(self):
        ...

    @abstractmethod
    def get_lottery_by_draw_date(self, draw_date: str):
        ...


class LotteryServiceV0(LotteryService):
    def __init__(self,
                 lottery_repository: LotteryRepository,
                 purchased_lottery_repository: PurchasedLotteryRepository):
        super().__init__(lottery_repository=lottery_repository,
                         purchased_lottery_repository=purchased_lottery_repository)

    def purchase_lottery(self, purchase_mode: str):
        if purchase_mode == "1":
            winning_numbers, bonus_number = generate_lottery_numbers()
        else:
            numbers = map(int, input("구매할 숫자를 중복없이 7자 입력하세요 (Ex. 1,2,3,4,5,6,7): ").split(","))
            winning_numbers = numbers[:-2]
            bonus_number = numbers[-1]

        purchased_lottery = PurchasedLottery(
            winning_numbers=winning_numbers,
            bonus_number=bonus_number
        )

        self.purchased_lottery_repository.save_purchased_lottery(
            purchased_lottery=purchased_lottery
        )

    def check_lottery(self):
        pass

    def get_all_lottery(self):
        return self.lottery_repository.find_all_lottery()

    def get_lottery_by_draw_date(self, draw_date: str):
        pass
