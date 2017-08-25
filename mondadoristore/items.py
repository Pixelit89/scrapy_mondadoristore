# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MondadoristoreItem(scrapy.Item):    
    isbn = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()