# -*- coding: utf-8 -*-
import scrapy
from MiniAppArticleSpider.items import WxItem
import json


class BaiduSpider(scrapy.Spider):
    """
    百度小程序社区爬虫
    """
    name = "baidu"
    allowed_domains = ["smartprogram.baidu.com"]
    start_urls = ['https://smartprogram.baidu.com/forum/api/forum_home']

    def parse(self, response):
        post_data = json.loads(response.body)
        if post_data and post_data['data'] and post_data['data']['topicList']:
            for post_item in post_data['data']['topicList']:
                title = post_item['title']
                href = 'https://smartprogram.baidu.com/forum/topic/show/{}'.format(post_item['topicId'])
                desc = ''
                url = href
                item = WxItem()
                item['title'] = title
                item['url'] = url
                item['desc'] = desc
                item['tags'] = ''
                item['author'] = ''
                item['ext'] = ''
                item['source'] = '2'
                yield item
            pass
