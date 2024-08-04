from controllers import LotteryController
from services import LotteryServiceV0
from repositories import LotteryRepositoryV0, PurchasedLotteryRepositoryV0


def main():
    lr_v0, plr_v0 = LotteryRepositoryV0(), PurchasedLotteryRepositoryV0()
    ls_v0 = LotteryServiceV0(lottery_repository=lr_v0, purchased_lottery_repository=plr_v0)
    lc = LotteryController(lottery_service=ls_v0)

    while True:
        try:
            mode = input("모드를 선택하세요\n"
                         "1. 로또 구매\n"
                         "2. 로또 결과 조회\n"
                         "3. 회차별 로또 번호 조회\n"
                         "4. 전체 회차 로또 번호 조회\n"
                         "종료를 원하시면 Ctrl + C를 눌러주세요\n")
        except KeyboardInterrupt:
            print("로또 시스템이 종료됩니다.")
            break

        if mode == "1":
            lc.purchase_lottery()
        elif mode == "2":
            lc.search_lottery_result()
        elif mode == "3":
            lc.search_lottery_by_round_number()
        elif mode == "4":
            lc.search_all_lotteries()
        else:
            print("{0}값이 입력되었습니다. 1 ~ 4 사이의 숫자를 입력해 주세요".format(mode))


if __name__ == "__main__":
    main()
