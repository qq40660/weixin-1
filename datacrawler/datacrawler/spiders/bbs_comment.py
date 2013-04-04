# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.utils.url import urljoin_rfc
from scrapy.http import Request
from bbs.items import bbsItem
from scrapy.item import Item, Field 

class bbsSpider(BaseSpider):

    name = "comment"
    allowed_domains = ["bbs.nju.edu.cn"]
    start_urls = ["http://bbs.nju.edu.cn/bbstop10"]


    def parseContent(self,comment):    
        commentorIndex =comment.index(unicode('信区','utf-8'))
        commentor = comment[4: commentorIndex-2]
        timeIndex = comment.index(unicode('南京大学小百合站 (','utf-8'))
        time = comment[timeIndex+10:timeIndex+34]
        comment = comment[timeIndex+37:]
        return (commentor,time,comment)


    def parse2(self,response):
        hxs =HtmlXPathSelector(response)
        item = response.meta['item']
        items=response.meta['items']
        #item['commentor'] = hxs.select('/html/body/center/table[position()>1]/tr[2]/td/textarea/text()').extract()
        comment = hxs.select('/html/body/center/table[position()>1]/tr[2]/td/textarea/text()').extract()

       
        list_commentor=[]
        list_time=[]
        list_comment=[]

        for i in comment:
            parseTuple = self.parseContent(i)
            #print parseTuple
            list_commentor.append(parseTuple[0])
            list_time.append(parseTuple[1])
            list_comment.append(parseTuple[2])

            #print item['commentor'] 

        length=len(list_comment)
        item_commentor=Field()
        item_time=Field()
        item_comment=Field()
        for i in  range(0,length):
            item_commentor[i]=list_commentor[i]
            item_time[i]=list_time[i]
            item_comment[i]=list_comment[i]

        item['commentor']=item_commentor
        item['comment_time']=item_time
        item['comment']=item_comment

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



           