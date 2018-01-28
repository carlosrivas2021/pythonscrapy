import scrapy




class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://cruises.bookits.club/web/cruises/results.aspx?',

        ]
        for url in urls:
            yield scrapy.Request(url=url, cookies={
                'ASP.NET_SessionId': 'xzntujkxpu43oopdomt2qhpq'
            }, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.item-list'):
            yield {
                'text': quote.css('div.departure-icon strong::text').extract(),
                'author': response.css('nobr a::attr(href)').extract_first(),
                'tags': 'Prueba',
            }
        next_page = response.css('nobr a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin('https://cruises.bookits.club/web/cruises/results.aspx?',next_page)
            yield scrapy.Request(next_page, callback=self.parse)
