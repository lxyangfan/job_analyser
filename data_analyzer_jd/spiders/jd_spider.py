# -*- coding: utf-8 -*-
import pdb
import scrapy
import ConfigParser
import os
import urllib
from scrapy import Request
from data_analyzer_jd.items import JobDetailItem

liepin_config = ConfigParser.ConfigParser()
# Assuming it is at the same location
fp = os.path.abspath(os.path.dirname(
    os.path.abspath(__file__)) + '/../../liepin.cfg')
liepin_config.read(fp)


class JobDetailSpider(scrapy.Spider):
    name = 'jb'
    allowed_domains = ['liepin.com']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        keyword = urllib.quote(liepin_config.get('search', 'keyword'))
        url = 'https://www.liepin.com/zhaopin/?d_pageSize=40&industries=040&dqs=020&d_curPage=1&key=%s' % keyword
        yield Request(url, headers=self.headers)

    def parse(self, response):
        jobs_xpath = '/html/body[@id="sojob"]//div[@class="sojob-item-main clearfix"]'
        for sel in response.xpath(jobs_xpath):
            job = sel.xpath('div[@class="job-info"]')
            job_detail_url = job.xpath(
                'h3/a/@href').extract_first(default='Null').strip()
            if job_detail_url != 'Null':
                if job_detail_url.startswith('http'):
                    yield Request(job_detail_url, headers=self.headers)
                elif job_detail_url.startswith('/'):
                    yield Request('%s%s' % ('https://www.liepin.com', job_detail_url), headers=self.headers)
            # 产生下一页地址
            next_xpath = '//div[@class="pagerbar"]/a[@class="current"]/following-sibling::a[1]'
            # 下一页不是disable了，说明还没头
            if response.xpath(next_xpath + '/text()').extract_first().strip() != u'下一页':
                yield Request('https://www.liepin.com' + response.xpath(next_xpath + '/@href').extract_first().strip(), headers=self.headers)

        one_job = "/html/body/div[@id='job-view-enterprise']"
        if response.xpath(one_job):
            item = JobDetailItem()
            item['job_id'] = response.url.split("?", 2)[0]
            item['job_title'] = response.xpath(
                "/html//div[@id='job-view-enterprise']//div[@class='title-info']/h1/text()").extract_first().strip()
            item['job_req'] = response.xpath(
                "/html//div[@class='job-qualifications']").extract_first().strip()
            item['salary'] = response.xpath(
                "/html//p[@class='job-item-title']/text()").extract_first().strip()
            item['address'] = response.xpath(
                "/html//ul[@class='new-compintro']/li[3]").extract_first().strip()
            item['education'] = response.xpath(
                "/html//div[@class='job-qualifications']/span[1]/text()").extract_first().strip()
            item['experience'] = response.xpath(
                "/html//div[@class='job-qualifications']/span[2]/text()").extract_first().strip()
            item['job_desp'] = response.xpath(
                "/html//div[@class='about-position ']/div[@class='job-item main-message'][1]/div[@class='content content-word']").extract_first().strip()
            item['comp_id'] = response.xpath(
                "/html//div[@class='title-info']/h3/a/@href").extract_first().strip()
            item['comp_size'] = response.xpath(
                "//ul[@class='new-compintro']/li[2]/text()").extract_first().strip()
            item['comp_name'] = response.xpath(
                "/html//div[@class='title-info']/h3/a/text()").extract_first().strip()
            yield item

        one_hunter_job = "/html/body/div[@id='job-hunter']"
        if response.xpath(one_hunter_job):
            item = JobDetailItem()
            item['job_id'] = response.url.split("?", 2)[0]
            item['job_title'] = response.xpath(
                "/html/body/div[@id='job-hunter']/div[@class='wrap clearfix']/div[@class='clearfix content']/div[@class='main']/div[@class='about-position ']/div[@class='title']/div[@class='title-info ']/h1/text()").extract_first().strip()
            item['job_req'] = response.xpath(
                "/html/body/div[@id='job-hunter']//div[@class='resume clearfix']").extract_first().strip()
            item['salary'] = response.xpath(
                "/html/body/div[@id='job-hunter']//p[@class='job-main-title']/text()").extract_first().strip()
            item['education'] = response.xpath(
                "/html/body/div[@id='job-hunter']//div[@class='resume clearfix']/span[1]/text()").extract_first().strip()
            item['experience'] = response.xpath(
                "/html/body/div[@id='job-hunter']//div[@class='resume clearfix']/span[2]/text()").extract_first().strip()
            item['job_desp'] = response.xpath(
                "/html/body/div[@id='job-hunter']//div[@class='content content-word']").extract_first().strip()
            yield item
