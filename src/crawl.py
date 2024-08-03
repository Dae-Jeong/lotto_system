from controllers import CrawlController
from services import LotteryServiceV0, SeleniumCrawlerService
from repositories import LotteryRepositoryV0, PurchasedLotteryRepositoryV0


def crawl():
    lottery_repository = LotteryRepositoryV0()
    purchased_lottery_repository = PurchasedLotteryRepositoryV0()

    lottery_service = LotteryServiceV0(lottery_repository=lottery_repository,
                                       purchased_lottery_repository=purchased_lottery_repository)

    selenium_crawler_service = SeleniumCrawlerService(lottery_repository=lottery_repository)

    crawl_controller = CrawlController(lottery_service=lottery_service,
                                       crawler_service=selenium_crawler_service)

    crawl_controller.crawl_winning_lottery()


if __name__ == "__main__":
    crawl()
