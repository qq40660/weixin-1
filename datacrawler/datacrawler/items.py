# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DatacrawlerItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass

class BookItem(Item):
    title = Field()
    author = Field()
    publisher = Field()
    index = Field()
    booktype = Field()
    link = Field()
    img_url = Field()
    intro = Field()
    borrow_status = Field()


class bbsItem(Item):
    title = Field()
    link = Field()
    text=Field()
    author = Field()
    content = Field()
    board = Field()
    time = Field()
    commentor =Field()
    comment =Field()
    comment_time=Field()



