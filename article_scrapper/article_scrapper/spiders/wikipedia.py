import scrapy


class WikipediaSpider(scrapy.Spider):
    name = 'wikipedia'
    allowed_domains = ['en.wikipidia.org']
    start_urls = ['http://en.wikipidia.org/']

    def parse(self, response):
        pass
