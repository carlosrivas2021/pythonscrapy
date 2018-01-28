import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from mercado.items import MercadoItem

class MercadoSpider(CrawlSpider):
    name = "mercado"
    item_count = 0
    allowed_domain = ['www.mercadolibre.com.ve']
    start_urls = ['https://listado.mercadolibre.com.ve/impresoras#D[A:impresoras]']

    rules = {
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="results-section"]/div[2]/ul/li[12]/a') )),
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//li[@class="results-item article grid item-info-height-117"]') ), callback= 'parse_item', follow = False),
    }

    def parse_item(self, response):
        yield {
            'titulo': response.xpath('normalize-space(//*[@id="short-desc"]/div/header/h1)').extract(),
            'precio': response.xpath('normalize-space(//*[@id="productInfo"]/fieldset[1]/span/span[2])').extract()   
        }
        self.item_count += 1
        if self.item_count > 10:
            raise CloseSpider('item_exceeded')
            
        