# -*- coding: utf-8 -*-

import os

array = ['wx', 'aliPay', "Tnfe -s USER_AGENT='CCBot'", 'wxapp']
command = ''
for index, val in enumerate(array):
    command += 'scrapy crawl ' + val
    if index < len(array) - 1:
        command += ' && '
print command
os.system(command)
