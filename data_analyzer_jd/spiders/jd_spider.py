# -*- coding: utf-8 -*-
import scrapy


class JobDetailSpider(scrapy.Spider):
    name = 'jbspider'
    allowed_domains = ['liepin.com']
    start_urls = [
        'https://www.liepin.com/zhaopin/?d_curPage=0&d_pageSize=40&industries=040&dqs=020&key=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90++%E6%8C%96%E6%8E%98'
    ]

    def parse(self, response):
        jobs_xpath = '/html/body[@id="sojob"]/div[@class="container"]/div[@class="wrap"]/div[@class="job-content"]/div/ul/li/div'
        for sel in response.xpath(jobs_xpath):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print title, link, desc