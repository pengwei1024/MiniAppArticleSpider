# -*- coding: utf-8 -*-
import scrapy
from MiniAppArticleSpider.items import WxItem


class WxSpider(scrapy.Spider):
    """
    https://github.com/Tnfe/TNFE-Weekly
    """
    name = "Tnfe"
    allowed_domains = ["github.com"]
    start_urls = ['https://github.com/Tnfe/TNFE-Weekly/blob/master/README.md']

    def parse(self, response):
        quotes = response.css('ol>li')
        for post_item in quotes:
            title = post_item.css('a::text').extract_first()
            href = post_item.css('a::attr(href)').extract_first()
            url = response.urljoin(href)
            item = WxItem()
            item['title'] = title
            item['url'] = url
            item['desc'] = u'腾讯新闻前端团队-TNFE'
            item['tags'] = ''
            item['author'] = ''
            item['ext'] = ''
            item['source'] = '5'
            yield item
