# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from bs4 import BeautifulSoup as bs
import re
import pdb

class HtmlTagRemovePipeline(object):
    
    def process_item(self, item, spider):
        for key in item.keys():
            if not item[key].startswith('http'):
                item[key] = self.remove_tag(item[key])
        return item

    def remove_tag(self, raw):
        return bs(raw).text


class TransFormItemPipeline(object):
    
    def process_item(self, item, spider):
        self.transForm(item)
        return item

    def transForm(self, item):
        ptn_str = u'(\d+)-(\d+)万'
        ptn = re.compile(ptn_str)
        if ptn.match(item['salary']):
            gg = ptn.search(item['salary'])
            item['salary_min'] = gg.group(1)
            item['salary_max'] = gg.group(2)