# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class HelloscrapyPipeline(object):
    def __init__(self):
        self.create_connection()
        
    def create_connection(self):
        self.conn = sqlite3.connect('database.db')
        self.curr = self.conn.cursor()

    def process_item(self, item, spider):
        self.store_relationaldb(item)
        return item
    
    def store_relationaldb(self, item):
        self.curr.execute("""INSERT INTO scrapy_tb VALUES(?,?,?)""",(item['title'][0],item['author'][0],item['tag'][0]))
        self.conn.commit()