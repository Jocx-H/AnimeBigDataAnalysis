# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BlibliItem(scrapy.Item):
    # 索引页的ajax 可以获得以下信息:
    url = scrapy.Field()                 # 详情url
    title = scrapy.Field()               # 标题
    cover = scrapy.Field()               # 封面

