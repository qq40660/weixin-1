# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.utils.url import urljoin_rfc
from scrapy.http import Request
from datacrawler.items import BookItem

class BookSpider(BaseSpider):
    name = "book"
    #allowed_domains = ["lib.nju.edu.cn"]
    start_urls = [
            "http://202.119.47.8:8080/opac/search_adv_result.php?sType0=any&q0=python&pageSize=100&sort=score&desc=true"
            ]

    def parse2(self, response):
        hxs = HtmlXPathSelector(response)

        item = response.meta['item']
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

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//table/tr[position()>1]')
        items = []
        for site in sites:
            item = BookItem()
            item['title'] = site.select('td[2]/a/text()').extract()
            link = site.select('td[2]/a/@href').extract()[0]
            result_link = urljoin_rfc('http://202.119.47.8:8080/opac/', link)
            item['link'] = result_link
            item['author'] = site.select('td[3]/text()').extract()
            item['publisher'] = site.select('td[4]/text()').extract()
            item['index'] = site.select('td[5]/text()').extract()
            item['booktype'] = site.select('td[6]/text()').extract()
            items.append(item)
        
        for item in items:
            yield Request(item['link'],meta={'item':item},callback=self.parse2)
