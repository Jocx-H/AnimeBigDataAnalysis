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
    allowed_domains = ['dmzj.com']

    # 索引页的ajax
    request_url = 'https://www.dmzj.com/category/1-0-0-0-0-0-{}.html'
    index = 1
    start_urls = [request_url.format(index)]

    def parse(self, response):
        list_data = response.xpath('//ul[@class="list_con_li"]/li')
        for data in list_data:
            item = BlibliItem()
            item['url'] = data.xpath('.//a//@href').extract_first()
            item['cover'] = data.xpath('.//a//img//@src').extract_first()
            item['title'] = data.xpath('.//span//h3//a//text()').extract_first()
            item['last_short_title'] = data.xpath('.//span//p[4]//text()').extract_first()
            item['author'] = data.xpath('.//span//p[1]//text()').extract_first()
            item['type'] = data.xpath('.//span//p[2]//text()').extract_first()
            item['state'] = data.xpath('.//span//p[3]//text()').extract_first()
            yield item
        self.index += 1   # 生成下一页的请求
        time.sleep(0.05)  # 休眠0.05s，防止触发反爬
        if self.index == 100:
            return
        yield scrapy.Request(url=self.request_url.format(self.index),
                             callback=self.parse)