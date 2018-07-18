# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MzituScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题 用来给本地的文件夹起名字的
    name = scrapy.Field()
    # 图片的链接
    image_urls = scrapy.Field()
    # 一个主题的链接 用来下载的时候加refer
    url = scrapy.Field()
    pass
