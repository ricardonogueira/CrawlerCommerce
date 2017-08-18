# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerextraItem(scrapy.Item):
	# define the fields for your item here like:
	name = scrapy.Field()
	page_size = scrapy.Field()
	image_size = scrapy.Field()
	css_size = scrapy.Field()
	js_size = scrapy.Field()
	text_size = scrapy.Field()
