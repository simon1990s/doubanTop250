# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class DoubanPipeline(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        print('开始爬虫')
        # 链接数据库
        self.conn = pymysql.Connect(host='10.0.0.128', port=3306, user='simon', password='letmein', db='db001',
                                    charset='utf8')

    # 编写向数据库中存储数据的相关代码
    # print('before process_item')

    def process_item(self, item, spider):
        # 1.链接数据库
        print('in the process_item')
        # 2.执行sql语句
        sql = 'insert into doubanMoives(moive_guid,title,rate_number,details,famous_words)values(uuid(),%s,%s,%s,%s)' % (
            self.conn.escape(item['title']), self.conn.escape(item['rate_num']),
            self.conn.escape(item['details']), self.conn.escape(item['famous_words']))
        self.cursor = self.conn.cursor()
        print(sql)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        # 3.提交事务

        return item

    def close_spider(self, spider):
        print('爬虫结束')
        self.cursor.close()
        self.conn.close()
