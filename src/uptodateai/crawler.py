import time
from urllib.parse import urlparse
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class PagingIncremental(CrawlSpider):
    name = "docs"
    custom_settings = {
        'DOWNLOAD_DELAY': '0',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'DEPTH_LIMIT': '0',
        'AUTOTHROTTLE_ENABLED': 'True',
        'AUTOTHROTTLE_START_DELAY': '1',
        'AUTOTHROTTLE_MAX_DELAY': '3',
        "AUTOTHROTTLE_TARGET_CONCURRENCY": '1'
    }
    rules = (Rule(LinkExtractor(allow=r""), callback='parse', follow=True),)

    def __init__(self, url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.domain = urlparse(url).hostname
        self.domain_name = self.domain.split('.')[1]
        self.allowed_domains = [self.domain]
        self.start_urls = [url]

    def parse(self, response):
        item = {}
        item["url"] = response.url
        time.sleep(.1)
        yield item

def process_docs(url):
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0',
        'ITEM_PIPELINES': {
            'uptodateai.pipeline.MarkdownPipeline': 1,
        },
    })

    process.crawl(PagingIncremental, url=url)
    process.start(stop_after_crawl=True)