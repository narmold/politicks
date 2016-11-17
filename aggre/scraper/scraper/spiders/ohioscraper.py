from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from aggre.models import posts

class MySpider(BaseSpider):
    name = "ap"
    allowed_domains = ["ap.org"]
    start_urls = ["hosted.ap.org"]


    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//span[@class='pl']")
        for titles in titles:
            title = titles.select("a/text()").extract()
            link = titles.select("a/@href").extract()
            print title, link