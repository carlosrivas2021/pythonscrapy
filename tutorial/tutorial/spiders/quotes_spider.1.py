import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://cruises.bookits.club/web/cruises/category.aspx?brn=0.758754656072126b7960ca1df184c00bfa9b02f192408ee127459',
            
        ]
        for url in urls:
            yield scrapy.Request(url=url,cookies= {
            'ASP.NET_SessionId':'ci2xodarhwnkj134trwyxmaz'
        }, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)