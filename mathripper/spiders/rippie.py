from scrapy.spider import Spider
from scrapy.selector import Selector
from mathripper.items import MathRip

import html2text

class RippieSpider(Spider):
    name = 'webripper'
    allowed_domains = ["genealogy.ams.org/"]
    start_urls = list("http://www.genealogy.ams.org/id.php?id=" + str(i) for i in range(191625))
    #]
    #def __init__(self):
    #    self.page_number = 191625

   # def start_requests(self):
   #     for i in range (self.page_number, number_of_pages, -1):
   #         yield Request(url =  % i, callback=self.parse)

    def parse(self, response):

        sel = Selector(response)
        sites = sel.xpath('body')
        items = []

        for site in sites:
            item = MathRip()
            #url = start_url[0] + 'id.php?id=%d' % i
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
