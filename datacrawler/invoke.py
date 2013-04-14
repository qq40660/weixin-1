#encoding=utf-8

from scrapy import project,signals
from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess
from scrapy.xlib.pydispatch import dispatcher
from multiprocessing.queues import Queue

import multiprocessing

from datacrawler.spiders.bbs_spider import bbsSpider
class CrawlerWorker(multiprocessing.Process):
    def __init__(self,spider,result_queue):
        multiprocessing.Process.__init__(self)
        self.result_queue = result_queue

        self.crawler = CrawlerProcess(Settings)
        if not hasattr(project,'crawler'):
            self.crawler.install()
        self.crawler.configure()
        self.items = []
        self.spider = spider
        dispatcher.connect(self._item_passed,signals.item_passed)

    def _item_passed(self):
        self.crawler.crawl(self.spider)
        self.crawler.start()
        self.crawler.stop()
        self.result_queue.put(self.items)


result_queue = Queue()
crawler = CrawlerWorker(bbsSpider(domain="bbs.nju.edu.cn"),result_queue)
crawler.start()
for item in result_queue.get():
    print item
