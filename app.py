# coding=utf-8
from flask import Flask, jsonify
from flask import render_template
import sqlite3
import cgi
import socket

DATABASE = 'mini_app.db'
PAGE_SIZE = 10

app = Flask(__name__)


def escape(html):
    """
    转义HTML字符
    :param html:
    :return:
    """
    if not html:
        return ""
    return cgi.escape(html)


def source_name(source):
    if source == "3":
        return u"支付宝"
    elif source == "4":
        return u"小程序社区"
    elif source == "5":
        return u"TNFE"
    return u"微信"


@app.route('/post/<int:page>')
def get_post(page=0):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.execute("select * from articles order by update_time desc limit {},{}".format(
        page * PAGE_SIZE, PAGE_SIZE))
    data = []
    for row in cursor.fetchall():
        item = {'title': row[1], 'href': row[2], 'desc': escape(row[3]), 'time': row[9],
                'source': source_name(row[7])}
        data.append(item)
    cursor.close()
    return jsonify(data)


@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.execute("select * from articles order by update_time desc limit {}".format(PAGE_SIZE))
    data = []
    for row in cursor.fetchall():
        item = {'title': row[1], 'href': row[2], 'desc': escape(row[3]), 'time': row[9],
                'source': source_name(row[7])}
        data.append(item)
    cursor.close()
    return render_template('index.Jinja2', data=data)


if __name__ == '__main__':
    host_name = socket.getfqdn(socket.gethostname())
    # 除了服务器都开启调试
    is_debug = 'centos' not in host_name
    app.run(host='0.0.0.0', debug=is_debug)
