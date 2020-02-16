# xml_str = "//div[@id='fh5co-bio']/div"
# from lxml import etree
# import re
#
# with open("./text.html", "r", encoding="utf-8") as f:
#     html = f.read()
#
# HTML = etree.HTML(html)
# p = HTML.xpath(xml_str)
# print(p)
#
# for div in p:
#     res = div.xpath("./h2/text()")[0]
#     # res = re.findall(r'''<h2.*?">(.*?)</h2>''', div.xpath("//*")[0])
#     print(res)
