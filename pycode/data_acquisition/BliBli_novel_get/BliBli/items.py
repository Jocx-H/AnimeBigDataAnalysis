#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BlibliItem(scrapy.Item):
    # 索引页的ajax 可以获得以下信息:
    url = scrapy.Field()                 # 详情url
    title = scrapy.Field()               # 小说名
    cover = scrapy.Field()               # 小说封面
    score = scrapy.Field()               # 小说评分
    author = scrapy.Field()              # 小说作者
    type = scrapy.Field()                # 小说类型
    introduce = scrapy.Field()           # 小说简介

