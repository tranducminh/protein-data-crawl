# -*- coding: utf-8 -*-
import scrapy


class ProteinsSpider(scrapy.Spider):
    name = 'proteins'
    allowed_domains = ['www.ncbi.nlm.nih.gov']
    start_urls = []
    with open("/Users/ducminh/Desktop/protein_data_crawl/protein_data_crawl/spiders/proteinList.txt", "r") as f:
        proteins = f.readlines()
        for protein in proteins:
            start_urls.append(
                f"https://www.ncbi.nlm.nih.gov/protein/{protein}")

    def parse(self, response):
        code = response.css(".rprtheader .itemid::text").get().split(" ")[-1]
        name = response.css(".rprtheader h1::text").get()
        yield {
            "code": code,
            "name": name
        }
