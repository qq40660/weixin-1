# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.utils.url import urljoin_rfc
from scrapy.http import Request
from datacrawler.items import bbsItem

class bbsSpider(BaseSpider):

    name = "comment"
    allowed_domains = ["bbs.nju.edu.cn"]
    start_urls = ["http://bbs.nju.edu.cn/bbstop10"]


    def parseContent(self,comment):
        print comment
        commentorIndex =comment.index(unicode(',','gbk'))
        commentor = comment[4: commentorIndex-2]
        return (commentor)


    def parse2(self,response):
        hxs =HtmlXPathSelector(response)
        item = response.meta['item']
        items=response.meta['items']
        #item['commentor'] = hxs.select('/html/body/center/table[position()>1]/tr[2]/td/textarea/text()').extract()
        comment = hxs.select('/html/body/center/table[position()>1]/tr[2]/td/textarea/text()').extract()
        for i in comment:
            parseTuple = self.parseContent(i)
            print parseTuple
            item['commentor'] = parseTuple[0]
        return item


    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        items = []
        title= hxs.select('/html/body/center/table/tr[position()>1]/td[3]/a/text()').extract()
        url= hxs.select('/html/body/center/table/tr[position()>1]/td[3]/a/@href').extract()
        for i in range(0, 10):
            item = bbsItem()
            item['link']= urljoin_rfc('http://bbs.nju.edu.cn/', url[i])+'&start=-1'


            items.append(item)

        for item in items:
            yield Request(item['link'],meta={'item':item,'items':items},dont_filter=True,callback=self.parse2)




