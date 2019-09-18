# -*- coding: utf-8 -*-

import os
from util.util import send_msg

array = ['wx', 'aliPay', "Tnfe -s USER_AGENT='CCBot'", 'wxapp', 'baidu']
command = ''
for index, val in enumerate(array):
    command += 'scrapy crawl ' + val
    if index < len(array) - 1:
        command += ' && '
print command
os.system(command)
send_msg(u'小程序社区更新完成!!!')
