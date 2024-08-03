from services import LotteryService


class LotteryController:
    def __init__(self, lottery_service: LotteryService):
        self.lottery_service = lottery_service

    def control(self):
        pass

    def purchase_lottery(self):
        purchase_mode = input("구매할 로또를 입력하세요 (1. 자동, 2. 수동): ")
        self.lottery_service.purchase_lottery(purchase_mode=purchase_mode)
