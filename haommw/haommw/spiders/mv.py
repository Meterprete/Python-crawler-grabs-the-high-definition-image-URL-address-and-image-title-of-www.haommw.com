# -*- coding: utf-8 -*-
import scrapy
import re
from haommw.items import HaommwItem


class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['haommw.com']
    start_urls = ['http://www.haommw.com/']

    def parse(self, response):
        div_list = response.xpath("//div[@id='fh5co-bio']/div")[1:-2]

        '''取第一级分类标题'''
        tag_list = []
        for div in div_list:
            tag = div.xpath("./h2/text()").extract_first()
            tag_list.append(tag)
        for index in range(len(tag_list)):
            print("【{}】{}".format(index, tag_list[index]), end=" ")

        print("\n" + "-" * 160)

        '''获取输入的一级分类对应的索引'''
        one_tage_index = int(input("\r\n请输入待抓取的一级分类对应的前面【】中的数字：\n"))

        '''根据所以取出对应的分类，继续遍历二级目录'''
        li_list = div_list[one_tage_index].xpath("./ul/li")
        two_tag_list = []
        for li in li_list:
            li_dict = {}
            data_src = "http://www.haommw.com{}".format(li.xpath("./a/@href").extract_first())
            data_text = li.xpath("./a/text()").extract_first()
            li_dict['name'] = data_text
            li_dict['href'] = data_src
            two_tag_list.append(li_dict)
        for index in range(len(two_tag_list)):
            print("【{}】{}".format(index, two_tag_list[index]['name']), end="\t")

        '''获取用户输入的二级标签的索引值'''
        two_tage_index = int(input("\r\n请输入待抓取的二级分类对应的前面【】中的数字：\n"))

        '''获取索引其对应的连接，请求数据，进行数据提取'''
        finall_tag_url = two_tag_list[two_tage_index]['href']
        print(finall_tag_url)
        yield scrapy.Request(
            finall_tag_url,
            callback=self.parse_One_detail
        )

    def parse_One_detail(self, response):
        '''首先，需要更改原来的headers，还有，高清图藏在a标签里'''
        div_list = response.xpath("//div[@class='grid']/div")[1:]
        for div in div_list:
            '''可以取到图片链接，以及图片的标题'''
            item = HaommwItem()
            item['Image_Name'] = div.xpath("./a[1]/@title").extract_first()
            item['Image_Url'] = div.xpath("./a[1]/@data").extract_first()
            yield item

        '''进行Ajax请求下一页图片'''
        url = response.url + "0:0/ajax/1/page/2"
        # 如果请求的数据为空或者小于20，直接进入piplines
        yield scrapy.Request(
            url,
            callback=self.parse_Ajax_detail
        )

    def parse_Ajax_detail(self, response):
        print(response.status)
        if response.status in [200, 500]:
            strp = response.text
            res = re.findall(r'''data="(.*?)" class="image-popup" title="(.*?)"''', strp)
            for p in res:
                item = HaommwItem()
                item['Image_Url'] = p[0]
                item['Image_Name'] = p[1]
                yield item

            '''进行下一页url地址的请求'''
            url_temp = response.url[:-1]
            page = int(response.url[-1:]) + 1
            url = url_temp + str(page)
            yield scrapy.Request(
                url,
                callback=self.parse_Ajax_detail
            )
