# -*- coding: utf-8 -*-
import scrapy
from MiniAppArticleSpider.items import WxItem


class WxSpider(scrapy.Spider):
    """
    支付宝小程序社区爬虫
    """
    name = "aliPay"
    allowed_domains = ["openclub.alipay.com"]
    start_urls = ['https://developer.aliyun.com/group/alipay']

    def parse(self, response):
        quotes = response.css('.question-slide-question')
        for post_item in quotes:
            title = post_item.css('.title::text').extract_first()
            href = post_item.css('a::attr(href)').extract_first()
            desc = ''
            url = response.urljoin(href)
            item = WxItem()
            item['title'] = title
            item['url'] = url
            item['desc'] = desc
            item['tags'] = ''
            item['author'] = ''
            item['ext'] = ''
            item['source'] = '3'
            yield item
