# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BlibliItem(scrapy.Item):
    # 索引页的ajax 可以获得以下信息:
    season_id = scrapy.Field()           # 漫画编号
    url = scrapy.Field()                 # 详情url
    title = scrapy.Field()               # 标题
    cover = scrapy.Field()               # 漫画封面
    last_short_title = scrapy.Field()    # 最近更新标题
    author = scrapy.Field()              # 漫画作者
    type = scrapy.Field()                # 漫画类型
    state = scrapy.Field()               # 连载状态

