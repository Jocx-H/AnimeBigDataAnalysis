"""
@Author: CloudAndMist
"""
import scrapy
from BliBli.items import BlibliItem
import json
import re
from datetime import datetime
import time
import scrapy
from scrapy.spiders import CrawlSpider


class SpiderBlSpider(scrapy.Spider):
    name = 'spider_bl'
    allowed_domains = ['cosplay8.com']

    # 索引页的ajax
    request_url = 'http://www.cosplay8.com/pic/chinacos/list_22_{}.html'
    index = 1
    start_urls = [request_url.format(index)]

    def parse(self, response):
        list_data = response.xpath('//div[@class="pagew center hauto pic_list"]/ul[1]/li')
        for data in list_data:
            item = BlibliItem()
            item['url'] = 'http://www.cosplay8.com'+data.xpath('.//a//@href').extract_first()
            item['cover'] = 'http://www.cosplay8.com'+data.xpath('.//a//img//@src').extract_first()
            item['title'] = data.xpath('.//p//a//text()').extract_first()
            yield item
        self.index += 1   # 生成下一页的请求
        time.sleep(0.05)  # 休眠0.05s，防止触发反爬
        if self.index == 11:
            return
        yield scrapy.Request(url=self.request_url.format(self.index),
                             callback=self.parse)