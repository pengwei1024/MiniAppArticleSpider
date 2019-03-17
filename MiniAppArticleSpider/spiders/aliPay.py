# -*- coding: utf-8 -*-
import scrapy
from MiniAppArticleSpider.items import WxItem


class WxSpider(scrapy.Spider):
    """
    支付宝小程序社区爬虫
    """
    name = "aliPay"
    allowed_domains = ["openclub.alipay.com"]
    start_urls = ['https://openclub.alipay.com/index.php?c=thread&a=subforum&orderby=postdate&fid=66&theme=']

    def parse(self, response):
        quotes = response.css('.threadblock')
        for post_item in quotes:
            title = post_item.css('.contitle a::text').extract_first()
            href = post_item.css('.contitle a::attr(href)').extract_first()
            desc = post_item.css('.coninfotext::text').extract_first()
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
