# -*- coding: utf-8 -*-
import scrapy
from ITcast.items import  ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['http://www.itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        node_list=response.xpath("//div[@class='li_txt']")


        #用来储存所有的item字段
        for node  in node_list:
            # 创建item字段对象 用来储存信息
            item=ItcastItem()
            # extract（）将xpath对象转黄为unicode字符串
            name=node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()
            # 返回每个item数据   给管道文件

            item["name"]=name[0]
            item["title"]=title[0]
            item["info"]=info[0]
            yield  item
        #pass
