# @Time : 2022/3/28 23:35
# @Author : Xiao Linbo
# @FileName: main.py
# @Email : 594986240@qq.com
# @Software: PyCharm

# 1. requests 发送请求，从服务器获取数据
# 2. BeautifulSoup 解析整个页面的源代码

import requests
from bs4 import BeautifulSoup
import os

# 创建Image folder文件夹用保存图片
path = os.getcwd() + '\Image folder2'
folder = os.path.exists(path)
if not folder:
    os.makedirs(path)

# 爬取网站的第一件事，发送请求到服务器
url = 'https://www.umeitu.com/meinvtupian/meinvxiezhen/'
resp = requests.get(url)  # 从服务器拿到源码
resp.encoding = 'utf-8'  # 改变编码格式 <meta charset="utf-8">
# print(resp.text)
# 解析html
main_page = BeautifulSoup(resp.text, 'html.parser')
# 从页面找到某些东西
TypeList = main_page.find('div', attrs={'class': 'TypeList'})
aList = TypeList.find_all('a', attrs={'class': 'TypeBigPics'})

m = 1  # 一个页面共30个套图

for a in aList:
    # 发送请求进入子页面，进入到高清页面
    # print(a.get('href')) #/meinvtupian/meinvxiezhen/243450.htm
    # 子页面实际地址为 https://www.umeitu.com/meinvtupian/meinvxiezhen/243450.htm
    href = 'https://www.umeitu.com' + a.get('href')
    for n in range(1, 99):
        if n != 1:
            href = href.rsplit('.', 1)[0] + '_{}.htm'.format(n)

        resp1 = requests.get(href)
        if resp1.status_code == 404:
            break
        resp1.encoding = 'utf-8'
        # --------------------------------------------------------------------------------
        # 找到图片的真实路径
        child_page = BeautifulSoup(resp1.text, 'html.parser')
        ImageBody = child_page.find('div', attrs={'class': 'ImageBody'})
        img = ImageBody.find('img')
        src = img.get('src')
        # --------------------------------------------------------------------------------
        # 发送请求到到服务器，把图片保存到本地
        # 创建文件
        f = open(path + '\picture_{}_{}.jpg'.format(m, n), mode='wb')
        # wb表示写入的内容是非文本文件 w=write b=binary
        pict = requests.get(src).content  # 向外拿出图片的数据，而不是文本信息
        f.write(pict)  # 保存图片
        print('picture_{}_{}.jpg'.format(m, n), 'has been downloaded')

    m += 1
