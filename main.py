# -*- coding: utf-8 -*-

import time
import os
import requests
import json


def get_data(pagenumber, topic):
    url = "https://api.coolapk.com/v6/page/dataList?"

    """
    热门动态: popular
    最近回复：lastupdate_desc
    最新发布：dateline_desc
    """

    params = {'url': '#/feed/multiTagFeedList', 'listType': 'recommend', 'sIncludeTop': 1, 'hiddenTagRelation': 1,
              'ignoreEntityById': 1, 'tag': topic, 'page': pagenumber}

    headers = {
        'Cookie': 'SESSID=eeee658b85f53a43e521a984dc5b8a3fd4c92ff5',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                      'Mobile/15E148 (#Build; Apple; iPhone Xs Max; iOS16.3.1; 16.3.1) +iCoolMarket/5.1.4-2303311',
        'X-App-Token': '97ed31124142a6af1e93c9f0c43c0a1aD2sPWzFd9vmmhJSxQG3qNVTH9Cq2bA8w5l3A695m0CNB8Xcf0x643628e4',
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
    response = requests.get(url=url, params=params, headers=headers)
    print("----*****-----正在请求第{}页数据-----****----".format(pagenumber))
    return response


def get_image_url(data):
    image_dict = {}
    dict = json.loads(data)
    data = dict["data"]  # 获取data数据
    for i in range(0, len(data) - 1):
        data1 = data[i]
        foldername = ""  # 初始化foldername变量为空字符串
        if "username" in data1 and "id" in data1:
            username = data1["username"]
            fileid = data1["id"]
            foldername = username + "_" + str(fileid)
        if "picArr" in data1:
            imageurl = data1["picArr"]
            image_dict[foldername] = imageurl
    return image_dict


def add_dict(new_get_dict, topic):
    filename = '{}.json'.format(topic)
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write('{}')
            print("已创建文件{}.json".format(topic))
    with open('{}.json'.format(topic), 'r', encoding='utf-8') as infile:
        old_data = json.load(infile)
        print("正在获取原有的数据....")
    # 将新的字典数据添加到现有数据中
    old_data.update(new_get_dict)
    print("追加数据到{}.json文件".format(topic))
    # 将更新后的数据写入文件中
    with open('{}.json'.format(topic), 'w', encoding='utf-8') as outfile:
        json.dump(old_data, outfile, ensure_ascii=False, indent=4)
        print("将更新后的数据写{}.json文件中".format(topic))


if __name__ == '__main__':
    page = 1
    tag = "壁纸"
    while True:
        response = get_data(page, tag)
        # print(response.text)
        status_code = response.status_code
        if status_code == 403:
            print("The status code is:", status_code)
            break
        else:
            data = response.text
            url = get_image_url(data)
            add_dict(url, tag)
        page += 1
        print("*******************等待3秒*******************")
        time.sleep(3)

# # 遍历每个图片项，获取图片地址并下载
# for item in image_dict:
#     # 获取图片地址
#     img_url = item.find('img')['src']
#
#     # 发送GET请求并下载图片
#     img_response = requests.get(img_url)
#     with open(img_url.split('/')[-1], 'wb') as f:
#         f.write(img_response.content)


# print(image_dict)

# 遍历字典里面的内容
# for key, value in image_dict.items():
#     print(key, value)
