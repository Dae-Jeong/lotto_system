from utils import generate_lottery_numbers
from controllers import LotteryController
from services import LotteryServiceV1


def main():
    winning_numbers, bonus_number = generate_lottery_numbers()
    print(winning_numbers)
    print(bonus_number)


if __name__ == "__main__":
    controller = LotteryController(lottery_service=LotteryServiceV1())
    main()
