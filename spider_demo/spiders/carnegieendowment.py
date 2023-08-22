import scrapy
# from ..items import CarnegieEndowmentPostItem


class CarnegieendowmentSpider(scrapy.Spider):
    name = "carnegieendowment"
    allowed_domains = ["carnegieendowment.org"]
    start_urls = ["https://carnegieendowment.org/publications/search-results?maxrow=20&tabName=pubs&channel=all&qry=&fltr=%7C&fltr=%7C&fltr=%7B%21raw+f%3DtaxonomyTag%7D%3A%3A1279%3A1531%3ATechnology&fltr=%7C&fltr=%7C"]

    def parse(self, response):
        # item = CarnegieEndowmentPostItem()
        posters = response.css('.content-img.col-25::text').getall()
        titles = response.css('ul.clean-list h4 a::text').getall()
        descriptions = response.css('ul.clean-list li > p::text').getall()
        post_type_list = response.css('ul.clean-list div.meta::text').getall()
        post_date_list = response.css('ul.clean-list ul.meta .inline::text').getall()
        author_list = response.css('ul.clean-list ul.meta .inline-block::text').getall()
        urls = response.css('ul.clean-list h4 a::attr(href)').getall()
        print(
            'titles ->',
            titles,
            '\nposters ->',
            urls,
        )
