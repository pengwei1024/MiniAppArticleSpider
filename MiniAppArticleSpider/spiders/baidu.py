# -*- coding: utf-8 -*-
import scrapy
from MiniAppArticleSpider.items import WxItem


class BaiduSpider(scrapy.Spider):
    """
    百度小程序社区爬虫 (需要登录)
    """
    name = "baidu"
    allowed_domains = ["smartprogram.baidu.com"]
    start_urls = ['https://smartprogram.baidu.com/forum/topic/list/1']

    def parse(self, response):
        quotes = response.css('.f-list-post')
        for post_item in quotes:
            title = post_item.css('.f-list-topic-cont a::text').extract_first()
            href = post_item.css('.f-list-topic-cont a::attr(href)').extract_first()
            desc = post_item.css('.tag::text').extract_first()
            url = response.urljoin(href)
            item = WxItem()
            item['title'] = title
            item['url'] = url
            item['desc'] = desc
            item['tags'] = ''
            item['author'] = ''
            item['ext'] = ''
            item['source'] = '2'
            yield item
