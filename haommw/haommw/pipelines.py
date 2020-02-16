# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class HaommwPipeline(object):
    def open_spider(self, spider):
        print("Mongodb is establishing a connection....................")
        client = MongoClient()
        self.connect = client['haommw']['data']
        print("\n===================================================================================")
        print("\n---------Name of the project: Beauty website picture crawler                     ||\n")
        print("---------author: Caiden_Micheal                                                  ||")
        print("---------GitHub address: https://github.com/Meterprete?tab=repositories          ||")
        print("---------Personal mailbox: wangxinqhou@foxmail.com                               ||")
        print("---------time: 2020.2.15                                                         ||\n")
        print("===================================================================================")

    def process_item(self, item, spider):
        self.connect.insert(dict(item))
        return item

    def close_spider(self, spider):
        print("程序执行完成。。。。。。。。")
