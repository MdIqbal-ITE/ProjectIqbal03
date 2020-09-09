#scrapy crawl Creative

# -*- coding: utf-8 -*-
import scrapy


class Project02Spider(scrapy.Spider):
    name = 'Project02'
    start_urls = ['http://192.168.150.135/creative']

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.json'
        with open(filename, 'wb') as f:
            f.write(response.body)
