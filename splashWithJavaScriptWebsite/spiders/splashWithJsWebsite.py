# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class SplashwithjswebsiteSpider(scrapy.Spider):
    name = 'splashWithJsWebsite'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/js/']

    def start_requests(self):
        # extract urls in webpage
        for url in self.start_urls:
            # request for each url visit
            yield SplashRequest(url=url,
                                callback=self.parse,
                                endpoint='render.html')

    def parse(self, response):
        # extract all quests
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            # one by one extract data from each of quote.
            yield {'author': quote.xpath('.//*[@class="author"]/text()').extract_first(),
                   'quote': quote.xpath('.//*[@class="text"]/text()').extract_first()}

        # script for javascript enable mouse click action for next  page
        script_mouseClick_action = """function main(splash)
                assert(splash:go(splash.args.url))
                splash:wait(0.3)
                button = splash:select("li[class=next] a")
                splash:set_viewport_full()
                splash:wait(0.1)
                button:mouse_click()
                splash:wait(1)
                return {url = splash:url(),
                        html = splash:html()}
            end"""

        # handling next page url
        yield SplashRequest(url=response.url,
                            callback=self.parse,
                            endpoint='execute',
                            args={'lua_source': script_mouseClick_action})
