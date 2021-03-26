import scrapy


class Covid19TotalBackupItem(scrapy.Item):
    date = scrapy.Field()
    country_in = scrapy.Field()
    country_out = scrapy.Field()
    total_country = scrapy.Field()
    capital_distance = scrapy.Field()
    noncapital_distance = scrapy.Field()
#    date_ = scrapy.Field()
    take_yesterday_1 = scrapy.Field()
    take_yesterday_2 = scrapy.Field()
    total_1 = scrapy.Field()
    total_2 = scrapy.Field()
    seoul_vaccine = scrapy.Field()
    gyeonggi_vaccine = scrapy.Field()
    incheon_vaccine = scrapy.Field()
