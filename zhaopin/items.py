# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZHIWEI(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  #职位名称
    catalog = scrapy.Field()  #职位类别
    location = scrapy.Field()  #职位地点
    number = scrapy.Field()  #招聘人数
    detaillink = scrapy.Field()  #详情页
    time = scrapy.Field()  #发布时间
