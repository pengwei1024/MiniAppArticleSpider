# -*- coding: utf-8 -*-
import scrapy
from MiniAppArticleSpider.items import WxItem


class WxSpider(scrapy.Spider):
    """
    微信小程序社区爬虫
    """
    name = "wx"
    allowed_domains = ["developers.weixin.qq.com"]
    start_urls = ['https://developers.weixin.qq.com/community/']

    def parse(self, response):
        quotes = response.css('.post_item')
        for post_item in quotes:
            title = post_item.css('.post_title a::text').extract_first()
            href = post_item.css('.post_title a::attr(href)').extract_first()
            desc = post_item.css('.post_desc::text').extract_first()
            url = response.urljoin(href)
            item = WxItem()
            item['title'] = title
            item['url'] = url
            item['desc'] = desc
            item['tags'] = ''
            item['author'] = ''
            item['ext'] = ''
            item['source'] = '1'
            yield item
