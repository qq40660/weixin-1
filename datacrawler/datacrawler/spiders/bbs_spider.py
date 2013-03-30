
# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.utils.url import urljoin_rfc

from bbs.items import bbsItem
 

class bbsSpider(BaseSpider):

    name = "bbs"
    allowed_domains = ["bbs.nju.edu.cn"]
    start_urls = ["http://bbs.nju.edu.cn/bbstop10"]

    def parse(self, response):
       hxs = HtmlXPathSelector(response)
       
       items = []
       title= hxs.select('/html/body/center/table/tr[position()>1]/td[3]/a/text()').extract()
       url= hxs.select('/html/body/center/table/tr[position()>1]/td[3]/a/@href').extract()
       for i in range(0, 10):
           item = bbsItem()
           item['link'] = urljoin_rfc('http://bbs.nju.edu.cn/', url[i])
           item['title'] =  title[i]
           print url
           items.append(item)
       return items
   
