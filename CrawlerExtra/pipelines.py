# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CrawlerextraPipeline(object):

	def process_item(self, item, spider):

		nome_arquivo = item["name"].split("http://www.extra.com.br/")

		if nome_arquivo[0] != "":
			nome_arquivo = "homepage.csv"
		else:
			nome_arquivo = nome_arquivo[1].replace("/", "-")+".csv"

		with open(nome_arquivo, "w") as arq:
			arq.write("URL;" + str(item["name"]) + "\n")
			arq.write("Tamanho da Pagina;"+ str(item["page_size"]) +"\n")
			arq.write("Tamanho total de Imagens;" + str(item["image_size"]) + "\n")
			arq.write("Tamanho total de CSS;" + str(item["css_size"]) + "\n")
			arq.write("Tamanho total de JS;" + str(item["js_size"]) + "\n")
			arq.write("Tamanho total de Texto;" + str(item["text_size"]) + "\n")
		return item
