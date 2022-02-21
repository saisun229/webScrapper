import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['https://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        title = response.css('span.title::text').get()
        dateFromMeta = response.xpath('/html/head/meta[@name="DC.Date.Issued"]/@content').get()
        authorName = response.xpath('//div/pre/span[@class="author-name"]/text()').get()
        authorAddress = response.xpath('//div/pre/span[@class="address"]/text()').get()
        authorPhone = response.xpath('//div/pre/span[@class="phone"]/text()').get()
        authorEmail = response.xpath('//div/pre/span[@class="email"]/text()').get()
        headings = response.xpath('//div/pre/div/span[@class="subheading"]/text()').getall()
        return {
                "title": title,
                "name": authorName,
                "address": authorAddress,
                "phone": authorPhone,
                "email": authorEmail,
                "headings": headings,
                "date": dateFromMeta
                }
