import scrapy

class FirstSpider(scrapy.Spider):
    #Não pode alterar o nome dessas duas variáveis
    name = 'spiderone'
    start_urls = [
                'http://quotes.toscrape.com/'
    ]
    
    def parse(self, response):
        all_div_quotes = response.css('div.quote')
        for item in all_div_quotes:
            title = item.css('span.text::text').extract()
            author = item.css('.author::text').extract()
            tag = item.css('.tag::text').extract()
            yield {'title': title, 'author': author, 'tag': tag }