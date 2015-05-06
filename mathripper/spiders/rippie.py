from scrapy.spider import Spider
from scrapy.selector import Selector
from mathripper.items import MathRip

import html2text

class RippieSpider(Spider):
    name = 'webripper'
    allowed_domains = ["genealogy.math.ndsu.nodak.edu/"]
    start_urls = list("http://genealogy.math.ndsu.nodak.edu/id.php?id=" + str(i) for i in range(191625))
    
    def parse(self, response):

        sel = Selector(response)
        sites = sel.xpath('body')
        items = []

        for site in sites:
            item = MathRip()
            name_sample = sel.xpath('//*[@id="paddingWrapper"]/h2').extract()[0]
            school_sample = sel.xpath('//*[@id="paddingWrapper"]/div[2]/span/span').extract()[0]
            year_sample = sel.xpath('//*[@id="paddingWrapper"]/div[2]/span/text()[2]').extract()[0]

            converter = html2text.HTML2Text()
            converter.ignore_links = True

            item['name'] = converter.handle(name_sample).encode('ascii', 'ignore')
            item['school'] = converter.handle(school_sample).encode('ascii', 'ignore')
            item['year'] = converter.handle(year_sample).encode('ascii', 'ignore')
            item['url'] = response.url
            items.append(item)

        return items
