# -*- coding: utf-8 -*-

import configparser
import requests
import os
import json


def __read_data():
    """
    读取配置信息
    :return:
    """
    global config_file
    config_list = ['config-release.ini', 'config-debug.ini', 'config.ini']
    for name in config_list:
        config_file = './config/{}'.format(name)
        if os.path.exists(config_file):
            break
        else:
            config_file = None
    if not config_file:
        return None, None, None
    cf = configparser.ConfigParser()
    cf.read(config_file)
    section = cf.sections()
    key = 'msg'
    if section:
        return cf.get(key, 'request_url'), cf.get(key, 'request_params'), cf.get(key, 'content_field')
    return None, None, None


def send_msg(content):
    """
    发送消息
    :param content: 消息内容
    :return:
    """
    (url, data, field) = __read_data()
    if not url or not data:
        print "url={0}, data={1}".format(url, data)
        return
    headers = {'Content-Type': 'application/json'}
    json_content = json.loads(data)
    json_content[field] = content
    print json_content
    response = requests.post(
        url=url,
        headers=headers, data=json.dumps(json_content))
    print(response.content)
