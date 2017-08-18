# -*- coding: utf-8 -*-
import json
import scrapy
from haralyzer import HarPage
from scrapy.linkextractors import LinkExtractor
from scrapy_splash import SplashRequest
from CrawlerExtra.items import CrawlerextraItem

class ExtraSpider(scrapy.Spider):
	name = 'CrawlerExtra'

	def start_requests(self):
		yield SplashRequest("http://www.extra.com.br",
			callback=self.parse_item,
			endpoint="render.json",
			args={
				"wait":1,
				"har": 1,
				"html": 1,
			})

	def convertHar(self, body):
		meu_json = json.dumps(body, indent=4, sort_keys=True)
		return json.loads(meu_json)['har']

	def parse_item(self, response):

		# Obter e converter informação para o formato HAR (HTTP ARchive)
		#har = self.convertHar(response.data)
		har_page = HarPage("1", har_data=self.convertHar(response.data))

		item = CrawlerextraItem()
		# Obter informações dos elementos da página
		item['name'] = response.url
		item['page_size'] = har_page.page_size
		item['image_size'] =  har_page.image_size
		item['css_size'] = har_page.css_size
		item['js_size'] = har_page.js_size
		item['text_size'] = har_page.text_size
		yield item

		# Navegar pelos links extraídos
		links = LinkExtractor(restrict_xpaths=('//ul[contains(@class, "nav-list")]'), deny_domains=('deliveryextra.com.br')).extract_links(response)

		for link in links:
			yield SplashRequest(link.url,
				callback=self.parse_item,
				endpoint="render.json",
				args={
					"wait":1,
					"har": 1,
					"html": 1,
				})
