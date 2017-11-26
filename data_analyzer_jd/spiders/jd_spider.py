# -*- coding: utf-8 -*-
import scrapy
import pdb
from data_analyzer_jd.items import JobDetailItem

class JobDetailSpider(scrapy.Spider):
    name = 'jb'
    allowed_domains = ['liepin.com']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    def start_requests(self):
        url = 'https://www.liepin.com/zhaopin/?d_curPage=0&d_pageSize=40&industries=040&dqs=020&key=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90++%E6%8C%96%E6%8E%98'
        yield Request(url, headers=self.headers)

    def parse_page(self, response):
        jobs_xpath = '/html/body[@id="sojob"]/div[@class="container"]/div[@class="wrap"]/div[@class="job-content"]/div/ul/li/div[@class="sojob-item-main clearfix"]'
        for sel in response.xpath(jobs_xpath):
            job = sel.xpath('div[@class="job-info"]')
            item = JobDetailItem()
            item['job_id'] = job.xpath('h3/a/@href').extract_first(default='Null').strip()
            item['job_title'] = job.xpath('h3/a/text()').extract_first(default='Null').strip()
            item['job_req'] = job.xpath('p[@class="condition clearfix"]/@title').extract_first(default='Null').strip()
            # item.salary = job.xpath('a/text()').extract()
            # item.address = job.xpath('a/text()').extract()
            # item.education = job.xpath('a/text()').extract()
            # item.experience = job.xpath('a/text()').extract()
            # item.job_desp = job.xpath('a/text()').extract()

            comp = sel.xpath('div[@class="company-info nohover"]')
            item['comp_id'] = comp.xpath('p[@class="company-name"]/a/@href').extract_first(default='Null').strip()
            item['comp_name'] = comp.xpath('p[@class="company-name]/a/text()"]').extract_first(default='Null').strip()
            # item.comp_detail = sel.xpath('a/text()').extract()
            yield item
    
    def parse_one_job(self, response):
        pass

    def parse(self, response):
        self.parse_page(response)
        self.parse_one_job(response)
        