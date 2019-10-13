# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

class HelloscrapyPipeline(object):
    def __init__(self):
        self.mongoclient = MongoClient('localhost', 27017)
        self.db = self.mongoclient.thedatasocietydb
        
    def process_item(self, item, spider):
        self.db.scrapy_col.insert(dict(item))
        return item
