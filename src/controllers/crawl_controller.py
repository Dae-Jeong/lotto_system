from services import CrawlerService, LotteryService


class CrawlController:
    def __init__(self, crawler_service: CrawlerService, lottery_service: LotteryService):
        self.crawler_service = crawler_service
        self.lottery_service = lottery_service

    def crawl_winning_lottery(self):
        self.crawler_service.crawl_winning_lottery()
