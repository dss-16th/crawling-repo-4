import scrapy


class CovidSupportItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()
