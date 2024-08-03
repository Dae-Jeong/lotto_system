from abc import ABC, abstractmethod

from models import Lottery


class LotteryRepository(ABC):
    @abstractmethod
    def find_lottery(self):
        ...

    @abstractmethod
    def find_all_lottery(self):
        ...

    @abstractmethod
    def save_lottery(self, lottery: Lottery):
        ...


class LotteryRepositoryV0(LotteryRepository):
    def find_lottery(self):
        pass

    def find_all_lottery(self):
        pass

    def save_lottery(self, lottery: Lottery):
        print(lottery)
