# -*- coding:utf-8 -*-
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from DouBanBook.items import DoubanbookItem
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class BookhunterSpider(CrawlSpider):
    name = 'bookHunter'
    allowed_domains = ['book.douban.com']
    start_urls = ['http://book.douban.com/tag/%E7%BC%96%E7%A8%8B']

    rules = (
        Rule(SgmlLinkExtractor(allow=[r'/subject/\d+/$']), callback='parse_item', follow=True),
    )

    def parse_intro(self, intro_html):
        t = intro_html
        intro = t[t.find('<p>'):t.rfind('</p>')+4]  # drop head and foot
        p = intro.find('<p>')
        result = ''
        while p != -1 :
            q = intro.find('</p>')
            result += intro[p+3:q] + '\n'
            intro = intro[q+4:]
            p = intro.find('<p>')
        return result
    
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        book = DoubanbookItem()
        info = ''
        try:
            info = hxs.select("//div[@id='info']").extract()[0].encode('utf-8')
        except IndexError:
            pass
        print '********************************'
        try:
            book['title'] = hxs.select("//h1/span[1]/text()").extract()[0]
        except IndexError:
            pass
        try:
            book['author'] = re.findall( u'作者</span>:.*?>(.+?)</a>'.encode('utf-8'), info, re.S )[0]
        except IndexError:
            pass
        try:
            book['publisher'] = re.findall(u'出版社:</span>(.+?)<br>'.encode('utf-8'), info )[0]
        except IndexError:
            pass
        try:
            book['numOfPages'] = re.findall(u'页数:</span>(.+?)<br>'.encode('utf-8'), info )[0]
        except IndexError:
            pass
        try:
            book['ISBN'] = re.findall(u'ISBN:</span>(.+?)<br>'.encode('utf-8'), info )[0]
        except IndexError:
            pass
        try:
            book['rating'] = hxs.select("//div[@id='interest_sectl']/div/p/strong/text()").extract()[0].strip()
        except IndexError:
            pass
        try:
            raw_intro_html = hxs.select("//div[@id='link-report']/span[2]/div").extract()[0]
        except IndexError:
            try:
                raw_intro_html = hxs.select("//div[@id='link-report']/div").extract()[0]
            except IndexError:
                pass
        book['intro'] = self.parse_intro(raw_intro_html)
        book['image_urls'] = hxs.select("//div[@id='mainpic']/a/@href").extract()
        print '@@@@@@@@@@@@@@@@@@@@@@@@@'
        print book['title']
        #print book['intro']
        print book['rating']
        print book['numOfPages']
        return book
