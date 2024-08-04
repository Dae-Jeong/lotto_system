from services import LotteryService


class LotteryController:
    def __init__(self, lottery_service: LotteryService):
        self.lottery_service = lottery_service

    def purchase_lottery(self):
        purchase_mode = input("구매할 로또를 입력하세요 (1. 자동, 2. 수동): ")
        self.lottery_service.purchase_lottery(purchase_mode=purchase_mode)

    def search_lottery_result(self):
        purchased_lottery_id = input("사용자의 로또 ID를 입력하세요: ")
        self.lottery_service.check_lottery(purchased_lottery_id=purchased_lottery_id)

    def search_lottery_by_round_number(self):
        round_number = int(input("조회할 회차를 입력하세요: "))
        lottery = self.lottery_service.get_lottery_by_round_number(round_number=round_number)

        print(f"{'회차':<10}{'날짜':<15}{'당첨 번호':<30}{'보너스 번호':<15}")
        print(lottery)

    def search_all_lotteries(self):
        lotteries = self.lottery_service.get_all_lottery()

        print(f"{'회차':<10}{'날짜':<15}{'당첨 번호':<30}{'보너스 번호':<15}")
        for lottery in lotteries:
            print(lottery)
