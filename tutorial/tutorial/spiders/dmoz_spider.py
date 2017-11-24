#!python2
# -*- coding: UTF-8 -*-

from scrapy.spider import BaseSpider
from ..items import DmozItem

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoztools.net"]
    start_urls = [
        "http://dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://dmoztools.net/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self,response):
        sites = response.css('.title-and-desc')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.css('.site-title').xpath('text()').extract()[0].strip()
            item['link'] = site.xpath('./a/@href').extract()[0].strip()
            item['desc'] = site.css('.site-descr').xpath('text()').extract()[0].strip()
            items.append(item)
        return items
