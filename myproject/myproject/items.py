# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

## 임의로 작성한 코드
class Headline(scrapy.Item):
    """
    뉴스 헤드라인을 나타내는 Items 객체
    """
    title = scrapy.Field()
    body = scrapy.Field()