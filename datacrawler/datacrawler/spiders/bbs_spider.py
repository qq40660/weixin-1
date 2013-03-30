# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector


from bbs.items import bbsItem
 

class bbsSpider(BaseSpider):

    name = "bbs"
    allowed_domains = ["bbs.nju.edu.cn"]
    start_urls = ["http://bbs.nju.edu.cn/bbstop10"]

    def parse(self, response):
       hxs = HtmlXPathSelector(response)
       items = []
       item = bbsItem()
       item['title'] = hxs.select('/html/body/center/table/tr[position()>1]/td[3]/a/text()').extract()
       item['link'] = hxs.select('/html/body/center/table/tr[position()>1]/td[3]/a/@href').extract()
       items.append(item)
       return items
