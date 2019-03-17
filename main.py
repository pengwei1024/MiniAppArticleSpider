# -*- coding: utf-8 -*-

from scrapy.cmdline import execute
import os

os.system('scrapy crawl wx && scrapy crawl aliPay')
# execute(['scrapy', 'crawl', 'wx'])
# execute(['scrapy', 'crawl', 'aliPay'])
