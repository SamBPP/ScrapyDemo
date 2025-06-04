import scrapy

class QuoteItem(scrapy.Item):
    """Container for quote information."""
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
