import scrapy

class FirstSpider(scrapy.Spider):
    #Não pode alterar o nome dessas duas variáveis
    name = 'spiderone'
    start_urls = [
                'http://quotes.toscrape.com/'
    ]
    
    def parse(self, response):
        all_div_quotes = response.css('div.quote')
        #title = response.css('div.quote').css('span.text::text').extract()
        title = all_div_quotes.css('span.text::text').extract()
        author = all_div_quotes.css('.author::text').extract()
        tag = all_div_quotes.css('.tag::text').extract()
        yield {'title': title, 'author': author, 'tag': tag }
