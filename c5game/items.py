# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class C5GameItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    chinese_name = scrapy.Field()
    img_url = scrapy.Field()
    normal_price = scrapy.Field()
    sale_price = scrapy.Field()
    color = scrapy.Field()
    type = scrapy.Field()
