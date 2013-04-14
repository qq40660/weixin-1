#encoding=utf-8

from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log

from datacrawler.spiders.bbs_spider import bbsSpider
spider = bbsSpider(domain="bbs.nju.edu.cn")
crawler = Crawler(Settings())
crawler.configure()
crawler.crawl(spider)
crawler.start()

log.start()
reactor.run()
