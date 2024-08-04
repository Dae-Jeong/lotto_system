import datetime
from abc import ABC, abstractmethod

from repositories import LotteryRepository, PurchasedLotteryRepository
from utils import generate_lottery_numbers, calculate_round_number
from models import PurchasedLottery, Lottery
from consts import LOTTERY_RESULT_MESSAGE_DICT
import uuid


class LotteryService(ABC):
    def __init__(self,
                 lottery_repository: LotteryRepository,
                 purchased_lottery_repository: PurchasedLotteryRepository):
        self.lottery_repository = lottery_repository
        self.purchased_lottery_repository = purchased_lottery_repository

    @abstractmethod
    def purchase_lottery(self, purchase_mode: str) -> None:
        ...

    @abstractmethod
    def check_lottery(self, purchased_lottery_id: str) -> None:
        ...

    @abstractmethod
    def get_all_lottery(self) -> list[Lottery]:
        ...

    @abstractmethod
    def get_lottery_by_round_number(self, round_number: int) -> Lottery:
        ...


class LotteryServiceV0(LotteryService):
    def __init__(self,
                 lottery_repository: LotteryRepository,
                 purchased_lottery_repository: PurchasedLotteryRepository):
        super().__init__(lottery_repository=lottery_repository,
                         purchased_lottery_repository=purchased_lottery_repository)

    def purchase_lottery(self, purchase_mode: str) -> None:
        if purchase_mode == "1":
            winning_numbers, bonus_number = generate_lottery_numbers()
        else:
            numbers = list(map(int, input("구매할 숫자를 중복없이 7자 입력하세요 (Ex. 1,2,3,4,5,6,7): ").split(",")))
            winning_numbers = numbers[:-1]
            bonus_number = numbers[-1]

        today = datetime.date.today().strftime("%Y-%m-%d")
        round_number = calculate_round_number(today=today)

        purchased_lottery = PurchasedLottery(
            purchased_lottery_id=str(uuid.uuid4()),
            round_number=round_number,
            winning_numbers=winning_numbers,
            bonus_number=bonus_number
        )

        self.purchased_lottery_repository.save_purchased_lottery(
            purchased_lottery=purchased_lottery
        )

        print("구매된 로또의 ID는 {0}입니다.".format(purchased_lottery.purchased_lottery_id))

    def check_lottery(self, purchased_lottery_id: str) -> None:
        find_purchased_lottery = self.purchased_lottery_repository.find_purchased_lottery_by_id(
            purchased_lottery_id=purchased_lottery_id
        )

        find_lottery = self.lottery_repository.find_lottery_by_round_number(find_purchased_lottery.round_number)
        result = find_lottery.check_lotto_result(user_winning_numbers=find_purchased_lottery.winning_numbers,
                                                 user_bonus_number=find_purchased_lottery.bonus_number)

        print(LOTTERY_RESULT_MESSAGE_DICT.get(result.name))

    def get_all_lottery(self) -> list[Lottery]:
        return self.lottery_repository.find_all_lottery()

    def get_lottery_by_round_number(self, round_number: int) -> Lottery:
        return self.lottery_repository.find_lottery_by_round_number(round_number=round_number)
