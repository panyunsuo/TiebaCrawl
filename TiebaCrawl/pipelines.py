# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class TiebaPipeline(object):
    def open_spider(self,spider):
        self.con=sqlite3.connect("sqlite.sqlite3")
        self.cur=self.con.cursor()
        sql="create table if not exists tieba(title varchar(100),content text)"
        self.cur.execute(sql)
    def close_spider(self,spider):
        self.con.close()
    def process_item(self, item, spider):
        sql=u"insert into tieba values('{0}','{1}')"
        sq=sql.format(item["title"],item["content"])
        self.cur.execute(sq)
        self.con.commit()
        return item
