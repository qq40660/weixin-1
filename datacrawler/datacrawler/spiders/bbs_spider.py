# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.utils.url import urljoin_rfc
from scrapy.http import Request
from datacrawler.items import bbsItem

class bbsSpider(BaseSpider):

    name = "bbs"
    #allowed_domains = ["bbs.nju.edu.cn"]
    start_urls = ["http://bbs.nju.edu.cn/bbstop10"]

    def parseContent(self,content):
        #content = content.encode('utf8')

        authorIndex =content.index(unicode('信区','gbk'))
        author = content[4:authorIndex-2]
        boardIndex = content.index(unicode('标  题','gbk'))
        board = content[authorIndex+4:boardIndex-1]
        timeIndex = content.index(unicode('南京大学小百合站 (','gbk'))
        time = content[timeIndex+10:timeIndex+34]
        content = content[timeIndex+37:]
        return (author,board,time,content)
    def parse2(self,response):
        hxs =HtmlXPathSelector(response)
        item = response.meta['item']
        try:
            content = hxs.select('/html/body/center/table[1]//tr[2]/td/textarea/text()').extract()[0]

            parseTuple = self.parseContent(content)
        except:
            return item
        item['author'] = parseTuple[0]
        item['board'] =parseTuple[1]
        item['time'] = parseTuple[2]
        item['content'] = parseTuple[3]
        return item
    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        items = []
        title= hxs.select('/html/body/center/table/tr[position()>1]/td[3]/a/text()').extract()
        url= hxs.select('/html/body/center/table/tr[position()>1]/td[3]/a/@href').extract()
        for i in range(0, 10):
            item = bbsItem()
            item['link'] = urljoin_rfc('http://bbs.nju.edu.cn/', url[i])

            item['title'] =  title[i][:-1]

            items.append(item)

        #return items
        for item in items:
            request = Request(item['link'],meta={'item':item},dont_filter=True,callback=self.parse2)
            if request:
                yield request
            else:
                yield item


        #yield Request(items[4]['link'],meta={'item':items[9]},dont_filter=True,callback=self.parse2)



