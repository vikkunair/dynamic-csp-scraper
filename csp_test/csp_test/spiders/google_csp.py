import scrapy
from scrapy_splash import SplashRequest

class GoogleCspSpider(scrapy.Spider):
    name = 'google_csp'
    allowed_domains = ['www.news.google.com']
    start_urls = ['http://www.news.google.com/']

    script = '''
        function main(splash, args)

            assert(splash:go(args.url))
            assert(splash:wait(0.5))
            
            splash:select('button[aria-label="Accept all"]'):mouse_click()
            assert(splash:wait(3))
            
            return splash:html()
        end
             '''

    def start_requests(self):
        yield SplashRequest(url="https://www.news.google.com",callback=self.parse,endpoint='execute',args={"lua_source":self.script})

    def parse(self, response):
        print(response.body)
