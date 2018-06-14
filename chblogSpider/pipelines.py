# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem

class ChblogspiderPipeline(object):
    def __init__(self):
        self.file = open('cnblogs.json', 'w')
    def process_item(self, item, spider):
        if item['title']:
            line = json.dumps(dict(item)) + '\n'
            self.file.write(line)
            return item
        else:
            raise DropItem('Missing title in %s'%item)
