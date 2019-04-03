# -*- coding: utf-8 -*-
import scrapy
from MiniAppArticleSpider.items import WxItem


class WxSpider(scrapy.Spider):
    """
    小程序社区爬虫 www.wxapp-union.com
    """
    name = "wxapp"
    allowed_domains = ["www.wxapp-union.com"]
    start_urls = ['http://www.wxapp-union.com/']

    def parse(self, response):
        quotes = response.css('#itemContainer .recommend_article_list')
        length = len(quotes)
        for index in range(length):
            # 暂时先取前20条
            if index > 20:
                break
            post_item = quotes[index]
            title = post_item.css('.list_title a::text').extract_first()
            tag = post_item.css('.recommend_article_list_info .mr10::text').extract_first()
            href = post_item.css('.list_title a::attr(href)').extract_first()
            desc = post_item.css('.recommend_article_list_simple::text').extract_first()
            url = response.urljoin(href)
            item = WxItem()
            item['title'] = title
            item['url'] = url
            item['desc'] = desc
            item['tags'] = tag
            item['author'] = ''
            item['ext'] = ''
            item['source'] = '4'
            yield item
