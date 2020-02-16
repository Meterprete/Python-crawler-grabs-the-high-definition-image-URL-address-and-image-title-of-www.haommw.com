# import re
#
# with open("text.html", "r", encoding="utf-8") as f:
#     str = f.read()
#
# res = re.findall(r'''data=\\"(.*?)" class=\\"image-popup\\" title=\\"(.*?)"''', str)
#
# list = []
# for p in res:
#     dict = {}
#     dict['href'] = re.sub(r"\\", "", p[0])
#     dict['name'] = re.sub(r"\\", "", p[1])
#     list.append(dict)
#
# print(list)
# print(len(list))
