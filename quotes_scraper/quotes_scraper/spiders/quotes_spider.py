import scrapy
from ..items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            item = QuoteItem(
                text=quote.css("span.text::text").get(),
                author=quote.css("span small.author::text").get(),
                tags=quote.css("div.tags a.tag::text").getall(),
            )
            yield item

        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
