# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from copy import deepcopy
import urllib


class DangdangSpider(RedisSpider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    # start_urls = ['http://book.dangdang.com/']
    redis_key = "dangdang" # 实现分布式爬虫，所有的服务器只有一个能访问到这个starturl（类似pop的操作），当此次访问结束后，所有的服务器便加载request了

    def parse(self, response):
        #大分类分组
        div_list = response.xpath("//div[@class='con flq_body']/div")
        for div in div_list:
            item = {}
            item["b_cate"] = div.xpath("./dl/dt//text()").extract() #  假设<div>/r/n<p>文学</p></div>,xpath语法就会返回 ['\r\n','文学']这样的列表，所以下面部分的数据清洗是非常有必要的
            item["b_cate"] = [i.strip() for i in item["b_cate"] if len(i.strip())>0]
            #中间分类分组
            dl_list = div.xpath("./div//dl[@class='inner_dl']")
            for dl in dl_list:
                item["m_cate"] = dl.xpath("./dt//text()").extract()
                item["m_cate"] = [i.strip() for i in item["m_cate"] if len(i.strip())>0][0]
                #小分类分组
                a_list = dl.xpath("./dd/a")
                for a in a_list:
                    item["s_href"] = a.xpath("./@href").extract_first()
                    item["s_cate"] = a.xpath("./text()").extract_first()
                    if item["s_href"] is not None:
                        yield scrapy.Request(
                            item["s_href"],
                            callback=self.parse_book_list,
                            meta = {"item":deepcopy(item)}
                        )

    def parse_book_list(self,response):
        item = response.meta["item"]
        li_list = response.xpath("//ul[@class='bigimg']/li")
        for li in li_list:
            item["book_img"] = li.xpath("./a[@class='pic']/img/@src").extract_first()
            if item["book_img"] == "images/model/guan/url_none.png":
                item["book_img"] = li.xpath("./a[@class='pic']/img/@data-original").extract_first()
            item["book_name"] = li.xpath("./p[@class='name']/a/@title").extract_first()
            item["book_desc"] = li.xpath("./p[@class='detail']/text()").extract_first()
            item["book_price"] = li.xpath(".//span[@class='search_now_price']/text()").extract_first()
            item["book_author"] = li.xpath("./p[@class='search_book_author']/span[1]/a/text()").extract()  # extract()拿到的是一个列表
            item["book_publish_date"] = li.xpath("./p[@class='search_book_author']/span[2]/text()").extract_first() # extract_first()拿到的是字符串
            item["book_press"] = li.xpath("./p[@class='search_book_author']/span[3]/a/text()").extract_first()
            print(item)
        #下一页
        next_url = response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_url is not None:
            next_url = urllib.parse.urljoin(response.url,next_url)
            yield  scrapy.Request(
                next_url,
                callback=self.parse_book_list,
                meta = {"item":item}
            )



