#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BlibliItem(scrapy.Item):
    # 索引页的ajax 可以获得以下信息:
    season_id = scrapy.Field()      # 番剧编号
    media_id = scrapy.Field()       # 媒体编号
    title = scrapy.Field()          # 标题
    index_show = scrapy.Field()     # 集数
    is_finish = scrapy.Field()      # 是否完结
    video_link = scrapy.Field()     # 链接
    cover = scrapy.Field()          # 封面图
    pub_real_time = scrapy.Field()  # 真实发布日期
    renewal_time = scrapy.Field()   # 最近更新日期

    # 番剧信息的ajax请求:
    favorites = scrapy.Field()      # 追番
    coins = scrapy.Field()          # 硬币
    views = scrapy.Field()          # 播放量
    danmakus = scrapy.Field()       # 弹幕

    # 番剧详情页的ajax请求：
    cm_count = scrapy.Field()       # 评论数
    score = scrapy.Field()          # 评分
    media_tags = scrapy.Field()     # 类型标签
