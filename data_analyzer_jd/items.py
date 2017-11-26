# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DataAnalyzerJdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_id = scrapy.Field()
    job_title = scrapy.Field()
    salary = scrapy.Field()
    address = scrapy.Field()
    education = scrapy.Field()
    experience = scrapy.Field()
    job_desp = scrapy.Field()
    comp_id = scrapy.Field()
    comp_name = scrapy.Field()
    comp_detail = scrapy.Field()
