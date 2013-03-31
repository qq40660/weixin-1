# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from datacrawler.items import BookItem

class BookSpider(BaseSpider):
    name = "book2"
    allowed_domains = ["lib.nju.edu.cn"]
    start_urls = [
            "http://202.119.47.8:8080/opac/item.php?marc_no=0003174847"
            ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        item = BookItem()
        item['img_url'] = hxs.select('//body/div[4]/div/div[2]/div[2]/img/@src').extract()
        item['intro'] = hxs.select('//body/div[4]/div/div[2]/div/dl[13]/dd/text()').extract()

        borrow = []
        borrow_result = hxs.select('//body/div[4]/div/div[6]/table//tr[position()>1]')
        for b in borrow_result:
            status_item = {}
            address = b.select("td[4]/text()").extract()[0]
            status_item[address] = b.select("td[5]/text()").extract()
            borrow.append(status_item)
        item['borrow_status'] = borrow

        return item
