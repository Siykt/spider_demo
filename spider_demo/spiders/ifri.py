import scrapy


class IfriSpider(scrapy.Spider):
    name = "ifri"
    allowed_domains = ["ifri.org"]
    start_urls = ["https://www.ifri.org/fr/recherche/thematiques-transversales/geopolitique-technologies"]

    def parse(self, response):
        for post_el in response.css("#tab-publications article"):
            date = post_el.css('.date-vignette .text-resize-em::text').get().strip()
            poster = post_el.css('.image-vignette img::attr(src)').get().strip()
            title = post_el.css('.title-vignette-search a::attr(title)').get().strip()
            author = ''.join([x.strip() for x in post_el.css('.list-author *::text').getall()])
            description = post_el.css('.content-vignette p::text').get().strip()
            print(
                '\n-----------------------',
                '\ntitle ->',
                title,
                '\ndate ->',
                date,
                '\nposter ->',
                poster,
                '\nauthor ->',
                author,
                '\ndescription ->',
                description,
            )
