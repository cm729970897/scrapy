from scrapy import Spider,Request
from c5game.items import C5GameItem
import re

class c5gamespider(Spider):

    name = 'c5game'
    allowed_domains = ['c5game.com']
    start_urls = ['https://www.c5game.com/dota.html']
    base_url = 'http://www.c5game.com'

    def parse(self,response):
        item = C5GameItem()
        #max_page = response.xpath('[@id="content"]/div[1]/div[1]/div[2]/div/div[1])')
        max_page = response.xpath('[@id="content"]/div[3]/div')

        max_page = response.xpath('//*[@id="yw1"]/li[10]/a/@href').re('(\d+)')[0]
        # to_follow_urls = response.xpath('//*[@id="yw0"]/div[1]/ul/li/a/@href').extract()
        for i in range(1,int(max_page)+1):
            if i == 1:
                yield Request('https://www.c5game.com/dota.html',callback=self.parse_url)
            else:
                url = 'https://www.c5game.com/dota.html?page={}'.format(i)
                yield Request(url,callback=self.parse_url)

    def parse_url(self,response):
        to_follow_urls = response.xpath('//*[@id="yw0"]/div[1]/ul/li/a/@href').extract()
        for url in to_follow_urls:
            url_tmp = self.base_url + url
            yield Request(url_tmp,callback=self.parse_item)

    def parse_item(self,response):
        item = C5GameItem()
        item['chinese_name'] = response.xpath('//*[@id="content"]/div[1]/div[1]/div[2]/div/div[1]/span/text()').extract()[0]
        item['normal_price'] = response.xpath('//*[@id="content"]/div[1]/div[1]/div[2]/div/div[4]/span/text()').extract()[0]
        item['sale_price'] = response.xpath('//*[@id="sale-table"]/tr/td[3]/span/text()').extract()
        item['img_url'] = response.xpath('//*[@id="content"]/div[1]/div[1]/div[1]/img/@src').extract()[0]
        next_url = 'https://www.c5game.com/dota/item/index.html?item_id={}&type=S&locale=en'.format(re.search('(\d{2,15})',response.url).group(1))
        yield Request(next_url,callback=self.parse_other_item,meta={'item':item})

    def parse_other_item(self,response):
        item = response.meta['item']
        item['name']  = response.xpath('//*[@id="content"]/div[1]/div[1]/div[2]/div/div[1]/span/text()').extract()[0]
        yield item
        # https://www.c5game.com/dota/item/index.html?item_id=11738082&type=S&locale=en
        # https://www.c5game.com/dota/14926397-S.html
        # https://www.c5game.com/dota/item/index.html?item_id=14926397&type=S&locale=zh
        # for url in to_follow_urls:
        #     print(self.base_url+'/'+url)c
        # print(to_follow_urls)
        # print(len(to_follow_urls))
        # names = response.xpath('//*[@id="yw0"]/div[1]/ul/li/p[1]/a/span/text()').extract()
        # prices = response.xpath('//*[@id="yw0"]/div[1]/ul/li/p[2]/span[1]/span/text()').extract()
        # for name,price in zip(names,prices):
        #     item['name'] = name
        #     item['price'] = price
        #     yield item
        # for i in range(2,int(max_page)+1):
        #     url_l = self.base_url + '/dota.html?page=' + str(i)
            # yield Request(url_l,callback=self.parse_item)

    # def parse_item(self,response):
    #     item = C5GameItem()
    #     names = response.xpath('//*[@id="yw0"]/div[1]/ul/li/p[1]/a/span/text()').extract()
    #     prices = response.xpath('//*[@id="yw0"]/div[1]/ul/li/p[2]/span[1]/span/text()').extract()
    #     for name,price in zip(names,prices):
    #         item['name'] = name
    #         item['price'] = price
    #         yield item
