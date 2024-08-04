LOTTERY_MIN_NUMBER = 1
LOTTERY_MAX_NUMBER = 45
LOTTERY_COUNT = 7
LOTTERY_FIRST_DATE = "2002-12-07"
LOTTERY_URL = "https://www.lotto.co.kr/article/list/AC01"
LOTTERY_RESULT_MESSAGE_DICT = {
    "FIRST": "1등: 모든 숫자가 일치합니다!",
    "SECOND": "2등: 5개의 숫자와 보너스 숫자가 일치합니다!",
    "THIRD": "3등: 5개의 숫자가 일치합니다!",
    "FOURTH": "4등: 4개의 숫자가 일치합니다!",
    "FIFTH": "5등: 3개의 숫자가 일치합니다!",
    "NONE": "꽝: 당첨되지 않았습니다."
}

# First  => abs(datetime.today() - LOTTERY_FIRST_DATE) = 일 수 차이
# Second => (일 수 차이 // 7) + 1 = 회차
