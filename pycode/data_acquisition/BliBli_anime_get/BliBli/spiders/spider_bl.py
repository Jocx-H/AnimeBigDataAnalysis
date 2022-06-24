import scrapy
from BliBli.items import BlibliItem
import json
import re
from datetime import datetime
import scrapy
from scrapy.spiders import CrawlSpider


class SpiderBlSpider(scrapy.Spider):
    name = 'spider_bl'
    allowed_domains = ['bilibili.com']

    # 索引页的ajax
    request_url = 'https://bangumi.bilibili.com/media/web_api/search/result?page={}&season_type=1&pagesize=20'
    page = 1
    start_urls = [request_url.format(page)]

    # 番剧信息的ajax请求
    season_url = 'https://bangumi.bilibili.com/ext/web_api/season_count?season_id={}&season_type=1&ts={}'

    # 番剧详情页的ajax请求
    media_url = 'https://www.bilibili.com/bangumi/media/md{}'

    def parse(self, response):
        # if self.page == 2:  # 限制爬取页数，用于测试爬取状态
        #     return
        list_data = json.loads(response.text).get('result').get('data')
        if len(list_data) == 0: # 如果响应中没有数据，则结束执行
            return

        for data in list_data:
            ts = datetime.timestamp(datetime.now())
            yield scrapy.Request(url=self.season_url.format(data.get('season_id'), ts),
                                 callback=self.parse_details,
                                 meta=data)
        self.page += 1  # 生成下一页的请求
        yield scrapy.Request(url=self.request_url.format(self.page),
                             callback=self.parse)

    def parse_details(self, response):
        item = BlibliItem()

        meta_data = response.meta
        item['season_id'] = meta_data.get('season_id')
        item['media_id'] = meta_data.get('media_id')
        item['title'] = meta_data.get('title')
        item['index_show'] = meta_data.get('index_show')
        item['is_finish'] = meta_data.get('is_finish')
        item['video_link'] = meta_data.get('link')
        item['cover'] = meta_data.get('cover')
        item['pub_real_time'] = meta_data.get('order').get('pub_real_time')
        item['renewal_time'] = meta_data.get('order').get('renewal_time')

        resp_data = json.loads(response.text).get('result')
        item['favorites'] = resp_data.get('favorites')
        item['coins'] = resp_data.get('coins')
        item['views'] = resp_data.get('views')
        item['danmakus'] = resp_data.get('danmakus')

        yield scrapy.Request(url=self.media_url.format(item['media_id']),
                             callback=self.parse_media,
                             meta=item)

    def parse_media(self, response):
        item = response.meta

        resp = response.xpath('//div[@class="media-info-r"]')
        item['media_tags'] = resp.xpath('//span[@class="media-tags"]/span/text()').extract()
        try:
            item['score'] = resp.xpath('//div[@class="media-info-score-content"]/text()').extract()[0]
        except Exception:
            item['score'] = '暂无评分'
        try:
            item['cm_count'] = resp.xpath('//div[@class="media-info-review-times"]/text()').extract()[0]
        except Exception:
            item['cm_count'] = '0人评'

        yield scrapy.Request(url=item['video_link'],
                             callback=self.parse_intro,
                             meta=item)

    def parse_intro(self, response):
        item = response.meta

        try:
            item['introduce'] = response.xpath('//meta[@name="description"]/@content').extract_first()
            item['introduce'] = re.sub('[\n\t\r]', '', item['introduce'])
        except Exception:
            item['introduce'] = '暂无简介'

        yield item


