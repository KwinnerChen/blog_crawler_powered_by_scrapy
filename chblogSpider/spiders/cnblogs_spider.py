# -*- coding: utf-8 -*-

import scrapy

from chblogSpider.items import ChblogspiderItem


class CnblogsSpider(scrapy.Spider):
    # 爬虫的名称
    name = 'cnblogs'
    # 允许访问的域名
    allowed_domains = ['cnblogs.com']
    # 初始链接
    start_urls = ['http://www.cnblogs.com/qiyeboy/default.html?page=1']

    def parse(self, response):
        # 解析网页，使用Selector.xpath()选择器，返回内容列表
        papers = response.xpath('//*[@class="day"]')
        # 从每项中抽取需要的数据
        for paper in papers:
            url = paper.xpath('//*[@class="postTitle"]/a/@href').extract()[0]
            title = paper.xpath('//*[@class="postTitle"]/a/text()').extract()[0]
            time = paper.xpath('//*[@class="dayTitle"]/a/text()').extract()[0]
            content = paper.xpath('//*[@class="postTitle"]/a/text()').extract()[0]
            item = ChblogspiderItem(url=url, title=title, time=time, content=content)
            yield item
        next_page = scrapy.Selector(response=response).re(r'<a href="(\S*)">下一页<\a>')
        if next_page:
            yield scrapy.Request(url=next_page[0], callback=self.parse)
