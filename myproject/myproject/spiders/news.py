import scrapy

# Item의 Headline 클래스를 읽어 들입니다.
from myproject.items import Headline

class NewsSpider(scrapy.Spider):
    name = 'news'
    # 크롤링 대상 도메인 리스트
    allowed_domains = ['engadget.com']
    # 크롤링을 시작할 URL 리스트
    start_urls = ['http://engadget.com/']

    def parse(self, response):
        """
        메인 페이지의 토픽 목록에서 링크를 추출하고 출력합니다.
        """
        link = response.css('a.o hit_link::attr("href")').extract()