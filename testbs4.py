#bs4将html转换为四种节点的树状图
#Tag,NavigableString,BeautifulSoup,Comment
import re

from bs4 import BeautifulSoup
file=open("./baidu.html","rb")
html=file.read().decode("utf-8")
bs=BeautifulSoup(html,"html.parser")
'''
print(bs.head)
print(type(bs.head))
print(bs.title)
print(type(bs.title))
print(bs.title.string)
print(type(bs.title.string))
print(type(bs))
print(bs.a)
print(bs.a.attrs)    #按字典返回数据类型：属性值+内容
print(bs.a.string)
print(type(bs.a.string))
#Tag 按标签给内容，只会返回找到的第一个标签的内容
#NavigableString 标签里的内容
#BeautifulSoup 表示整个文档
#comment是特殊的NavigableString，不包含注释符号
'''

'''
#遍历文档
#contents是按列表返回Tag
print(bs.head.contents[0])
'''

'''
#搜索文档
#1.字符串过滤，查找与字符串完全匹配的内容标签
t_list=bs.find_all("div")
print(t_list)

#2.正则表达式搜索 search() 带a的标签都进了
t_list=bs.find_all(re.compile("a"))
for item in t_list:
    print(item)
#3.传入函数，根据函数的要求来搜索
#4.kwargs 参数
#bs.select
t_list=bs.find_all(class_=True)
for item in t_list:
    print(item)
#CSS选择器
'''