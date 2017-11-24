#!python2
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.spider import BaseSpider
from scrapy.http import Request
from ..items import DoubanspiderItem
import re

class DouBanSpider(BaseSpider):
    name = "douban"
    allowed_domains = ["https://movie.douban.com"]
    start_urls = ['https://movie.douban.com/chart']

    def parse(self, response):
        rank_links = response.css('.types').xpath('.//span/a/@href').extract()
        for rank_link in rank_links:
            print self.allowed_domains[0]+rank_link
            yield Request(self.allowed_domains[0]+rank_link,callback=self.parse_list,dont_filter=True)

    def parse_list(self,response):
        movie_list = response.css('.movie-list-panel list')
        for movie in movie_list:
            movie_link = movie.xpath('.//span/a/@href').extract()
            print self.allowed_domains[0]+movie_link
            yield Request(self.allowed_domains[0]+movie_link, callback=self.parse_movie,dont_filter=True)

    def parse_movie(self,response):
        print "88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888"
        print response