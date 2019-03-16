# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import sqlite3


class SQLitePipeline(object):
    __conn = None
    __cursor = None

    # 打开数据库
    def open_spider(self, spider):
        db_name = spider.settings.get('SQLITE_DB_NAME')
        table_create = spider.settings.get('SQLITE_TABLE_CREATE')
        self.__conn = sqlite3.connect(db_name)
        self.__conn.execute(table_create)
        self.__cursor = self.__conn.cursor()

    # 关闭数据库
    def close_spider(self, spider):
        self.__conn.commit()
        self.__conn.close()

    # 对数据进行处理
    def process_item(self, item, spider):
        self.__insert_db(item)
        return item

    # 插入数据
    def __insert_db(self, item):
        values = (
            item['title'],
            item['url'],
            item['desc'],
            item['tags'],
            item['author'],
            item['ext'],
            item['source'],
        )
        sql = 'INSERT INTO articles (title,url,desc,tags,author,ext,source) VALUES(?,?,?,?,?,?,?)'
        try:
            self.__cursor.execute(sql, values)
        except sqlite3.IntegrityError:
            pass
