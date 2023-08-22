# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarnegieEndowmentPostItem(scrapy.Item):
    title = scrapy.Field()
    poster = scrapy.Field()
    description = scrapy.Field()
    post_type = scrapy.Field()
    post_date = scrapy.Field()
    author = scrapy.Field()
    url = scrapy.Field()
