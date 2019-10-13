import scrapy

class FirstSpider(scrapy.Spider):
    #Não pode alterar o nome dessas duas variáveis
    name = 'spiderone'
    start_urls = [
                'http://quotes.toscrape.com/'
    ]
    
    def parse(self, response):
        yield {'pagina': response.text}