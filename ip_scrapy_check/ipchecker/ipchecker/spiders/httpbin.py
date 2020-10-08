import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = []
    start_urls = ['http://httpbin.org/get?show_env=1/']

    def parse(self, response):
        item = {}
        print(response)
        json_list = eval(response.text)
        item["User-Agent"] = json_list['headers']['User-Agent']
        item["origin"] = json_list["origin"]
        print(item)
        yield item


