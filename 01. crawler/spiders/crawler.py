import scrapy
import uuid, re, json, sys, os
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class AumItem(scrapy.Item):
    # define the fields for your item here like:
    urls = scrapy.Field()


class AUMSpider(scrapy.Spider):
    name = "ir"

    def __init__(self, start_urls, dir_name):
        self.start_urls = start_urls
        self.dir_name = dir_name

    def start_requests(self):
        urls = self.start_urls
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def extract_data(self, soup):

        try:
            cards = soup.find_all("div", id="tab-merchants")
            urls = cards[0].find_all("a", href=re.compile("place"))
            urls = ["" + url["href"] for url in urls]
        except Exception:
            pass
        return urls

    def parse(self, response):
        item = AumItem()
        if response.status >= 200 and response.status < 300:
            page = response.url.split("/")[-1].split("?")[0]
            filename = f"../data/{self.dir_name}/pages/{page}.html"
            with open(filename, "wb") as f:
                f.write(response.body)

            soup = BeautifulSoup(response.body, "html.parser")
            item["urls"] = self.extract_data(soup)
            yield item
        else:
            pass


def load_urls(path):
    f = open(path)
    file = json.load(f)
    return file


if __name__ == "__main__":

    un_crawled = load_urls("../data/ir/urls.json")["urls"]
    ## Create directories & files
    dir_name = "bestrestaurants"

    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(AUMSpider, start_urls=un_crawled, dir_name=dir_name)

    process.start()
    output = open("items.json")
    output = json.load(output)

    urls = []
    for idx in range(len(output)):
        urls.extend(output[idx]["urls"])

    data = {
        "urls": urls,
    }
    with open("../data/" + dir_name + "/urls2.json", "w", encoding="utf8") as fp:
        json.dump(data, fp, ensure_ascii=False)
