# -*- coding: utf-8 -*-

from scrapy.cmdline import execute
import os

os.system("scrapy crawl wx && scrapy crawl aliPay && scrapy crawl Tnfe -s USER_AGENT='CCBot' && scrapy crawl wxapp")
# execute(['scrapy', 'crawl', 'wx'])
# execute(['scrapy', 'crawl', 'aliPay'])
