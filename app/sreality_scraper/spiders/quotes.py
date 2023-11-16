import scrapy
from scrapy_playwright.page import PageMethod
from bs4 import BeautifulSoup

class SrealitySpider(scrapy.Spider):
    name = "test"

    def start_requests(self):
        urls = [
            "https://www.sreality.cz/hledani/prodej/byty/zahranici",
        ]
        for i in range(2, 25):
            urls.append("https://www.sreality.cz/hledani/prodej/byty/zahranici?strana=" + str(i))

        for url in urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                meta={
                    "playwright": True,
                    "playwright_page_methods": [
                        PageMethod("wait_for_selector", 'span.name'),
                    ],
                },
            )

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all("div", {"class": "property"})

        properties = []

        for i in data:
            property_soup = BeautifulSoup(str(i), 'html.parser')

            imgs = property_soup.find_all("img")
            
            name = property_soup.find("span", {"class": "name"}).text
            location = property_soup.find("span", {"class": "locality"}).text
            if len(imgs) > 0:
                print(name, location, imgs[0]['src'])
                properties.append((name, location, imgs[0]['src']))
        
        yield {"properties": properties}