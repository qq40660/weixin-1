# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from datacrawler.items import BookItem

class BookSpider(BaseSpider):
    name = "book"
    allowed_domains = ["lib.nju.edu.cn"]
    start_urls = [
            "http://202.119.47.8:8080/opac/search_adv_result.php?sType0=any&q0=ruby&pageSize=100&sort=score&desc=true"
            ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//table/tr')
        items = []
        for site in sites:
            item = BookItem()
            item['title'] = site.select('td[2]/a/text()').extract()
            item['author'] = site.select('td[3]/text()').extract()
            item['publisher'] = site.select('td[4]/text()').extract()
            item['index'] = site.select('td[5]/text()').extract()
            item['booktype'] = site.select('td[6]/text()').extract()
            items.append(item)
        return items


