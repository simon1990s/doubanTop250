# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from douban.items import DoubanItem


class Top250Spider(scrapy.Spider):
    name = 'top250'
    # allowed_domains = ['xxx']
    url = 'https://movie.douban.com/top250?start=%d&filter='
    url_number = 0
    start_urls = ['https://movie.douban.com/top250?start=%d&filter=' % url_number]

    # print('before parse')

    # def __init__(self):
    #     实例化一个浏览器对象(实例化一次)
    # self.bro = webdriver.Chrome(executable_path='C:\Users\Simon\Downloads\chromedriver_win32\chromedriver.exe')
    #
    # 必须在整个爬虫结束后，关闭浏览器
    # def closed(self, spider):
    #     print('爬虫结束')
    #     self.bro.quit()

    def parse(self, response):
        li_list = response.xpath('//div[@class="info"]')
        # print('长度%d' % len(li_list))
        for i, url_tmp in enumerate(li_list, 1):
            # url_xpath = '//*[@id="content"]/div/div[1]/ol/li[%d]/div/div[2]/div[1]/a'
            # url_tmp = url_tmp.xpath(url_xpath % i).extract_first()
            # new_url = url_tmp.split('"')[1]
            # print(new_url)
            # print(i)
            title = url_tmp.xpath(
                '//*[@id="content"]/div/div[1]/ol/li[%d]/div/div[2]/div[1]/a/span[1]/text()' % i).extract_first()
            rate_num = url_tmp.xpath(
                '//*[@id="content"]/div/div[1]/ol/li[%d]/div/div[2]/div[2]/div/span[2]/text()' % i).extract_first()
            details_tmp = url_tmp.xpath(
                '//*[@id="content"]/div/div[1]/ol/li[%d]/div/div[2]/div[2]/p[1]' % i)
            # string() 获取的是p标签下面的所有文本内容，包括<br>标签后面的，text()只能获取<br>标签前面的内容
            details = details_tmp.xpath('string()').extract()[0].strip().replace('\t', '').replace(' ', '')
            print('details %s ' % details)
            print(details.split('>'))
            famous_words = url_tmp.xpath(
                '//*[@id="content"]/div/div[1]/ol/li[%d]/div/div[2]/div[2]/p[2]/span/text()' % i).extract_first().replace(
                '\n', '', 100).replace('\t', '', 100)
            # print(rate_num, details, famous_words)
            items = DoubanItem()
            items['title'] = title
            items['rate_num'] = rate_num
            items['details'] = details
            items['famous_words'] = famous_words
            yield items

            if self.url_number < 225:
                self.url_number += 25
                new_url = format(self.url % self.url_number)
                yield scrapy.Request(url=new_url, callback=self.parse)
