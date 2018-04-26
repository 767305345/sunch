# -*- coding: utf-8 -*-
import scrapy


class DouyuzhuboinfoSpider(scrapy.Spider):
    name = 'douyuzhuboinfo'
    allowed_domains = ['douyucdn.cn']
    start_urls = ['http://douyucdn.cn/']

    def parse(self, response):
        pass
