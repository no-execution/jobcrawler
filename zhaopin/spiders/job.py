# -*- coding: utf-8 -*-
import scrapy
from zhaopin.items import ZHIWEI


class JobSpider(scrapy.Spider):
    name = 'job'
    preurl = []
    for i in range (35):
        url = 'http://hr.tencent.com/position.php?&start='+str(i*10)+'#a'
        preurl.append(url)
    start_urls = preurl

    def parse(self, response):
        #将items项目导入
        item = ZHIWEI()
        #获取总体内容
        KindInfo = response.css('tr[class*=even]')
        OddList = response.css('tr[class*=odd]')
        k = KindInfo+OddList
        jobname = response.css('tr a[target*="_blank"]::text').extract()
        link = response.css('tr a[target*="_blank"]::attr(href)').extract()
        #对总体内容进行信息提取
        for i in range(len(k)):
            gr1 = k[i].css('td::text').extract()
            item['name'] = jobname[i]
            item['detaillink'] = link[i]
            for j in range(len(gr1)):
                item['catalog'] = gr1[0]
                item['number'] = gr1[1]
                item['location'] = gr1[2]
                item['time'] = gr1[3]
            yield item



