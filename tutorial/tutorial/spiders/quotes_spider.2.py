import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://cruises.bookits.club/web/cruises/category.aspx?brn=0.758754656072126b7960ca1df184c00bfa9b02f192408ee127459',
            'https://cruises.bookits.club/web/cruises/category.aspx?brn=0.0827618344140993b7960ca1df184c00bfa9b02f192408ee127459',
            
        ]
        for url in urls:
            yield scrapy.Request(url=url,cookies= {
            'ASP.NET_SessionId':'ci2xodarhwnkj134trwyxmaz'
        }, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.categoryview-price-gride'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('span.price.percabinprice::text').extract(),
            }
        