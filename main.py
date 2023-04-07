# -*- coding: utf-8 -*-
import re

import requests
import json
from bs4 import BeautifulSoup

url = "https://api.coolapk.com/v6/page/dataList?"

"""
热门动态: popular
最近回复：lastupdate_desc
最新发布：dateline_desc
"""

params = {'url': '#/feed/multiTagFeedList', 'listType': 'dateline_desc', 'sIncludeTop': 1, 'hiddenTagRelation': 1,
          'ignoreEntityById': 1, 'tag': '美女壁纸', 'page': 1}

headers = {
    'Cookie': 'SESSID=eeee658b85f53a43e521a984dc5b8a3fd4c92ff5',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Mobile/15E148 (#Build; Apple; iPhone Xs Max; iOS16.3.1; 16.3.1) +iCoolMarket/5.1.4-2303311',
    'X-App-Token': '11b1ad450db05258a5c1ecc8864f6ae8D2sPWzFd9vmmhJSxQG3qNVTH9Cq2bA8w5l3A695m0CNB8Xcf0x642f9705',
    'Accept-Language': 'zh-Hans-US;q=1.0, en-US;q=0.9, ru-US;q=0.8, es-US;q=0.7, zh-Hant-US;q=0.6',
    'X-Sdk-Locale': 'zh-US',
    'X-Api-Version': '13',
    'X-App-Device': 'gXYNBycYBSZu9GaQlGI7UGbwBXQgsTZsBHcBByOgsDI7AyOmNGW4IkTDBTb1kjNBNDb1cHOBJmMxNUOIRlVOF3MHFFeTpEat1m'
                    'd5QmR6dFUzJDR',
    'X-App-Code': '2303311',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Sdk-Int': '16.3.1',
    'X-App-Version': '5.1.4',
    'X-App-Id': 'com.coolapk.app'

}
# 发送GET请求并获取响应
list = []
response = requests.get(url=url, params=params, headers=headers).text
dict = json.loads(response)
data = dict["data"]
# print(data)
image_list = {}

for i in range(0, len(data)-1):
    data1 = data[i]
    foldername = ""  # 初始化foldername变量为空字符串
    if "username" in data1 and "id" in data1:
        username = data1["username"]
        fileid = data1["id"]
        foldername = username+"_"+str(fileid)
    if "picArr" in data1:
        imageurl = data1["picArr"]
        image_list[foldername] = imageurl
print(image_list)


# tty = data[0]["message"]
# print(tty)
# text = re.search(r'(.*?)\n', tty).group(1)
# print(text)
# # print(data[0]["picArr"])

# # 将响应内容解码为UTF-8编码的文本
# content = response.content.decode('utf-8')
#
# # 将文本解析为HTML文档
# soup = BeautifulSoup(content, 'html.parser')
#
# # 查找所有class为"picture-list-item"的div标签
# picture_list_items = soup.find_all('div', class_='picture-list-item')
#
# # 遍历每个图片项，获取图片地址并下载
# for item in picture_list_items:
#     # 获取图片地址
#     img_url = item.find('img')['src']
#
#     # 发送GET请求并下载图片
#     img_response = requests.get(img_url)
#     with open(img_url.split('/')[-1], 'wb') as f:
#         f.write(img_response.content)
