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
import re
from scrapy.spiders import CrawlSpider


class SpiderBlSpider(scrapy.Spider):
    name = 'spider_bl'
    allowed_domains = ['book.sfacg.com']

    # 索引页的ajax
    request_url = 'https://book.sfacg.com/List/default.aspx?tid=-1&&&PageIndex={}'
    index = 1
    start_urls = [request_url.format(index)]

    def parse(self, response):
        list_data = response.xpath('//div[@class="comic_cover Blue_link3"]/ul')
        for data in list_data:
            item = BlibliItem()
            item['url'] = 'https://book.sfacg.com'+data.xpath('.//li[1]//a//@href').extract_first()
            item['cover'] = data.xpath('.//li[1]//a//img//@src').extract_first()
            item['title'] = data.xpath('.//li[2]//strong//a//text()').extract_first()
            item['author'] = data.xpath('.//li[2]/a[1]//text()').extract_first()
            item['score'] = data.xpath('.//li[2]/span/text()').extract_first()
            item['type'] = data.xpath('.//li[2]/a[2]/text()').extract_first()
            yield scrapy.Request(url=item['url'],
                                 callback=self.parse_details,
                                 meta=item)
        self.index += 1   # 生成下一页的请求
        time.sleep(0.05)  # 休眠0.05s，防止触发反爬
        if self.index == 500:
            return
        yield scrapy.Request(url=self.request_url.format(self.index),
                             callback=self.parse)

    def parse_details(self, response):
        data = response.xpath('//div[@class="count-detail"]//div[1]')
        item = response.meta
        item['state'] = data.xpath('.//span[2]/text()').extract_first()[3:]
        item['click_cnt'] = data.xpath('.//span[3]/text()').extract_first()[3:]
        item['update_time'] = data.xpath('.//span[4]/text()').extract_first()[3:]
        item['introduce'] = response.xpath('//p[@class="introduce"]/text()').extract_first()
        item['introduce'] = re.sub('[\n\t\r]', '',  item['introduce'])
        yield item