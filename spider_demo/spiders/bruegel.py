import scrapy


class BruegelSpider(scrapy.Spider):
    name = "bruegel"
    allowed_domains = ["bruegel.org"]
    start_urls = ["https://www.bruegel.org/search?topic%5B396%5D=396"]

    def parse(self, response):
        for post_el in response.css(".c-listing__items article"):
            date = post_el.css('.c-list-item__date::text').get().strip()
            title = post_el.css('.c-list-item__title a::text').get().strip()
            label = post_el.css('.c-list-item__content-label::text').get().strip()
            description = post_el.css('p.c-list-item__description::text').get().strip()
            print(
                '\n-----------------------',
                '\ntitle ->',
                title,
                '\ndate ->',
                date,
                '\nlabel ->',
                label,
                '\ndescription ->',
                description,
            )
