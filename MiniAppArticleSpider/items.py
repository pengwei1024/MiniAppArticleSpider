# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WxItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    desc = scrapy.Field()
    tags = scrapy.Field()
    author = scrapy.Field()
    ext = scrapy.Field()
    source = scrapy.Field()
