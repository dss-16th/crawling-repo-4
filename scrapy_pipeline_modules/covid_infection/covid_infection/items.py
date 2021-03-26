import scrapy


class CovidInfectionItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()
