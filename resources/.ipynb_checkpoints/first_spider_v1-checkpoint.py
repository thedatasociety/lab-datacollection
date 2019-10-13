import scrapy

class FirstSpider(scrapy.Spider):
    #Não pode alterar o nome dessas duas variáveis
    name = 'spiderone'
    start_urls = [
                'http://quotes.toscrape.com/'
    ]
    
    def parse(self, response):
        title = response.css('title').extract()
        #title = response.css('title::text').extract()
        yield {'titletext':title}