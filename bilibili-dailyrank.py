#-*- coding:utf-8 -*-             #使得代码可包含中文
import sys
from bs4 import BeautifulSoup     #网页解析，获取数据
import re                         #正则表达式，用于匹配文字
import urllib                     #指定url获取网页
import urllib.request
import xlwt                       #excel写入
import sqlite3                    #数据库操作
import gzip
from io import BytesIO


#提取格式
findLink = re.compile(r'href="//(.*?)"')  # 视频链接
findtitle = re.compile(r'blank">(.*?)</a')
findup = re.compile(r"</i>\n                (.*?)\n              </span>",re.S)
finddata = re.compile(r"</i>\n              (.*?)\n            </span>",re.S)

#获取信息
def askurl(url):
    #用户代理伪装成浏览器
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"}
    request = urllib.request.Request(url=url,headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

#处理并存储信息
def getData(baseurl):
    html = askurl(baseurl)  # 保存获取到的网页源码
    soup = BeautifulSoup(html, "html.parser")
    i = 1
    for item in soup.find_all('li', class_="rank-item"):# 查找符合要求的字符串
        item = str(item)
        link = re.findall(findLink, item)[0]
        worksheet.write(i, 1, label=link)
        title = re.findall(findtitle, item)[1]
        worksheet.write(i, 2, label=title)
        up = re.findall(findup,item)
        worksheet.write(i, 3, label=up)
        sc = re.findall(finddata, item)[1]
        worksheet.write(i, 4, label=sc)
        view = re.findall(finddata, item)[0]
        worksheet.write(i, 5, label=view)
        i += 1

if __name__ == "__main__":
    #建立excel存储模板
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('My Worksheet')
    worksheet.write(0, 0, label="rank")
    worksheet.write(0, 1, label="视频链接")
    worksheet.write(0, 2, label="视频名称")
    worksheet.write(0, 3, label="UP主名称")
    worksheet.write(0, 4, label="收藏数")
    worksheet.write(0, 5, label="播放量")
    for i in range(1,101):
        worksheet.write(i, 0, label=i)
    #干他妈的数据和存储
    getData("https://www.bilibili.com/v/popular/rank/all")
    workbook.save('bilibili_dailyrank.xls')
    print("数据爬取完毕")
    #建立excel存储模板
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('My Worksheet')
    worksheet.write(0, 0, label="rank")
    worksheet.write(0, 1, label="视频链接")
    worksheet.write(0, 2, label="视频名称")
    worksheet.write(0, 3, label="UP主名称")
    worksheet.write(0, 4, label="收藏数")
    worksheet.write(0, 5, label="播放量")
    for i in range(1,51):
        worksheet.write(i, 0, label=i)
    getData("https://www.bilibili.com/v/popular/rank/bangumi")
    workbook.save('bilibili_bangumirank.xls')
    print("数据爬取完毕")