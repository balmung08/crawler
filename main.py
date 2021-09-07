# -*- coding:utf-8 -*-             #使得代码可包含中文

import re  # 正则表达式，用于匹配文字
import urllib  # 指定url获取网页
import urllib.request
import requests
import json
import cv2
import tkinter
import tkinter.messagebox
import time
import datetime
x = 1
num = 0
zs = 10
z = 10

#触发登录框(用于刷新Authorization)
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73",
        "Referer":"https://pixivic.com/"}
url = "https://pagead2.googlesyndication.com/pagead/gen_204?id=sodar2&v=224&t=2&li=gda_r20210816&jk=1646750410345453&bg=!6Oul66_NAAZvV8FTb1c7ACkAdvg8WpsJduvkcBy9oIFetijRYbcPFlKlho-b6FJBoRxGuv8filjfgAIAAAB5UgAAAA5oAQcKABAQNwuYHNceBI7rTO4_iY95mQKsPZrwnwWKtZdDSnxdIr0W5k2CmbwZHnIUuYvSeGDLYQmvEdRcaaTtWw0lyDtqq-gmImLgj5s5FxbpM8XtkXPweFVlufzA6Tt734ELUr2wqTPmL2Pfin3Mu2rsuehjGlf5-lgmdpaTQBIXU6f52hqJwaNEX_gZnqqiC7b3rSEEhdwYuEZi_gAqlGhnKRgaunbVX5xBLbr1WSW_OjvOAS0GGnMvI1cVpqaE8-i5OqWgn5G-FrImv9TP1gUg8b3T0ZvzICZNRTRgBWFQIPvQLb3XdM3luulguyzimy_xHp2CadDpnJE3HohPHJ9byblegvPPrik1F0dyYrtwb5Didz_nk66Av1x3yNoHd7rS73q2b8vqAE-TPny8ZOG7XT-NRchNGbalz9E0UoIFE0x2RobFX6WiNEm5rJ56qG63gv7JKEgJGgNX93Vp5qmM1Zap4g9p5AQeCxiDY3HPYBsd1wulF0jjRnWD9OrkovZnw02ul3XcCgu8sxIhf8GdNGfq4QCxCMlxSXPgvR6t2HH4JZZtnuFRtbGL6aCr_RiIV4r2Y3A_rqJ-a9dMCRREk1_ozVJ6cH2UGosB5egujFxCmTRPwVkuUgLspI_6eLl_xA_fOpAW2elom1CfQgkvwgD08Coaw2t5osHs4lDEJDgqlxZrZIIbw9tS7APLBVv5TyKS08ItGta7tAEM5ou_Cq1k2358YpB-Y2D0GVHmaolzIa58rVb4QQb65npbhia5fOq__HcIQG7lsUhg_Pzlaw_0JiEtg_wCNP-6RkhQfSThVN9oeBmJl_7377NJqBtnz6uQ6CVnMZt9X734rZQMR8M2SezMD80qKgzjxtmx8LKQRI_BqyFnh9bB6ZzgJ4N5LLJvN0X9psNU8QqHiTGAf-IaLKzKsN9XBcIi9TmVTDWk"
request0 = requests.get(url=url,headers=headers)


#获取验证码
picurl  = "https://pix.ipv4.host/verificationCode"
request1 = urllib.request.Request(url=picurl, headers=headers)
response1 = urllib.request.urlopen(request1)
htmls = response1.read().decode('utf-8')
html = json.loads(htmls)
vid = html["data"]["vid"]
piurl = "data:image/bmp;base64," + html["data"]["imageBase64"]

#输出验证码
img = urllib.request.Request(url=piurl, headers=headers)
response1 = urllib.request.urlopen(img)
htmls = response1.read()
path = "1.jpg"
with open(path, 'wb') as f:
    f.write(htmls)

#识别验证码



#输入验证码(暂时)
img0 = cv2.imread("1.jpg")

#cv2.imshow("img0",img0)
#cv2.waitKey(0)
#value = input("验证码为：")


#交互界面设计

interaction = tkinter.Tk()
interaction.title("pixiv镜像爬图")
interaction.geometry("450x200")

'''
img_gif =tkinter.PhotoImage(file='./动作/问号.gif')  # 设置图片
label_img = tkinter.Label(interaction, image=img_gif)  # 设置预显示图片
label_img.place(x=30, y=120)
def change_img():   # 设置按钮事件
    img_gif0 = tkinter.PhotoImage(file='./动作/走.gif')
    label_img.configure(image=img_gif0)
    label_img.place(x=30, y=120)
'''
back=tkinter.PhotoImage(file="resource\\background.png")
tkinter.Label(image=back,anchor = 'nw').place(x=0,y=0)
text1 = tkinter.Label(interaction, text="    图片来源为pixiv镜像站pixic",font=20).place(x=10,y=0)
photo = tkinter.PhotoImage(file="1.jpg")
tkinter.Label(image=photo).place(x=70, y=35)
tkinter.Label(interaction,text="输入爬取tag：",font=20).place(x=10,y=105)
tag = tkinter.StringVar()
text2 = tkinter.Entry(interaction,textvariable=tag).place(x=150,y=105)
code = tkinter.StringVar()
tkinter.Label(interaction,text="验证码：",font=20).place(x=10,y=135)
yzm =tkinter.Entry(interaction,textvariable=code).place(x=150,y=135)


def fuzhi(zhi):
    zhi = int(zhi)
    global z
    z = zhi / 30
    tkinter.messagebox.showinfo('tip', '已选择张数：%d'%zhi)
def crawler():
    value = code.get()
    name = tag.get()
    urlname = urllib.parse.quote(name)
    #读取登录信息
    header = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73",
               "Referer": "https://pixivic.com/",
               "Path":"/users/token?vid="+vid+"&value="+value,
               "Content-Type": "application/json"
    }
    url = "https://pix.ipv4.host" + header["Path"]
    data = {'username': "", 'password': ""}
    req = requests.post(url=url, headers=header, json=data)
    authorization = req.headers["authorization"]
    print("loginover")

    def askurl(baseurl):
        head = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73",
             "Referer": "https://pixivic.com/",
             "Authorization":authorization}
        rem = urllib.request.Request(url=baseurl, headers=head)
        response1 = urllib.request.urlopen(rem)
        htm = response1.read().decode('utf-8')
        js = json.loads(htm)
        return js

    def getData(baseurl):
        html = askurl(baseurl)  # 保存获取到的网页源码
        tkinter.messagebox.showinfo('login', '登录成功，关闭此窗口后开始')
        num = 0
        l = 0
        li = html["data"][l]
        for i in html["data"]:
            li = html["data"][l]
            for n in li['imageUrls']:
                lj = n['original']
                findlink = re.compile(r'img-original/img/(.*)')
                link = re.findall(findlink, lj)
                urll = "https://o.acgpic.net/img-original/img/"+ "%s"%link[num]
                img = requests.get(urll, headers=headers,timeout=200000).content
                print(urll)
                global x
                find = re.compile("\\d{8}")
                id = re.findall(find, urll)
                find2 = re.compile("\\d{8}(.*)")
                p = re.findall(find2, urll)
                print(id,p)
                if len(id) == 0:
                    find3 = re.compile("\\d{7}")
                    id = re.findall(find3, urll)
                    find4 = re.compile("\\d{7}(.*)")
                    p = re.findall(find4, urll)
                path = "pic\\" + str(id[0]) + str(p[0])
                print(path)
                # 将图片写入指定的目录 写入文件用"wb"
                with open(path, 'wb') as f:
                    f.write(img)
                    print("正在下载第{}张图片".format(x))
                x += 1
            l += 1

    global z
    z = int(z)
    for i in range(1,z):
        i = str(i)
        url = "https://pix.ipv4.host/illustrations?illustType=illust&searchType=original&maxSanityLevel=3&page="+i+"&keyword=%s&pageSize=30"%urlname
        print(url)
        getData(url)

    tkinter.messagebox.showinfo('已完成爬取', '已完成爬取，十秒后退出')
    time.sleep(10)
    interaction.destroy()
def ar():
    tkinter.messagebox.showinfo('关于作者', '本程序来自balmung\n登录pixic所用账号为自建，所获取的数据不可用于盈利')
def he():
    tkinter.messagebox.showinfo('帮助', '验证码输错或看不清请关闭重开\ntag找不到也需关闭重开\ntag开始爬取会有提示')
def daily_he():
    tkinter.messagebox.showinfo('说明',"爬取p站前一日日榜前30")

    # 获取信息
def dc():
    def askurl(url):
        headers = {
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36x-requested-with: XMLHttpRequest',
            "Referer": 'https://pixivic.com/'
        }
        num = 0
        # 用户代理伪装成浏览器
        request = urllib.request.Request(url=url, headers=headers)
        html = ""
        try:
            response = urllib.request.urlopen(request)
            html = response.read().decode('utf-8')
            js = json.loads(html)


        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
        return js

    # 处理并存储信息
    def getData(baseurl):
        html = askurl(baseurl)  # 保存获取到的网页源码
        num = 0
        l = 0
        li = html["data"][l]
        for i in html["data"]:
            li = html["data"][l]
            for n in li['imageUrls']:
                lj = n['original']
                findlink = re.compile(r'img-original/img/(.*)')
                link = re.findall(findlink, lj)
                urll = "https://o.acgpic.net/img-original/img/" + "%s" % link[num]
                img = requests.get(urll, headers=headers).content
                global x
                find = re.compile("\\d{8}")
                id = re.findall(find, urll)
                find2 = re.compile("\\d{8}(.*)")
                p = re.findall(find2, urll)
                path = "daily\\" + str(id[0]) + str(p[0])
                # 将图片写入指定的目录 写入文件用"wb"
                with open(path, 'wb') as f:
                    f.write(img)
                    print("正在下载第{}张图片".format(x))
                x += 1
            l += 1
    i = datetime.datetime.now()
    y = i.year
    m = i.month
    d = i.day
    d -= 1
    url = "https://pix.ipv4.host/ranks?page=1&date="+"%02d-"%y+"%02d-"%m+"%02d"%d+"&mode=day&pageSize=30"
    try:
        getData(url)
    except Exception as e:
        y = i.year
        m = i.month
        d = i.day
        d -= 2
        url = "https://pix.ipv4.host/ranks?page=1&date="+"%02d-"%y+"%02d-"%m+"%02d"%d+"&mode=day&pageSize=30"
        getData(url)






menubar = tkinter.Menu(interaction)
filemenu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='爬取张数', menu=filemenu)
filemenu.add_command(label='30',command=lambda: fuzhi(30))
filemenu.add_command(label='60',command=lambda: fuzhi(60))
filemenu.add_command(label='90',command=lambda: fuzhi(90))
filemenu.add_command(label='120',command=lambda: fuzhi(120))
filemenu.add_command(label='150',command=lambda: fuzhi(150))
filemenu.add_command(label='180',command=lambda: fuzhi(180))
filemenu.add_command(label='210',command=lambda: fuzhi(210))
filemenu.add_command(label='240',command=lambda: fuzhi(240))
filemenu.add_command(label='270',command=lambda: fuzhi(270))
filemenu.add_command(label='300',command=lambda: fuzhi(300))
helpmenu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='帮助', menu=helpmenu)
helpmenu.add_command(label='关于',command=lambda: ar())
helpmenu.add_command(label='说明',command=lambda: he())
daily = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='日榜', menu=daily)
daily.add_command(label='说明',command=lambda: daily_he())
daily.add_command(label='go',command=lambda: dc())
interaction.config(menu = menubar)
botton = tkinter.Button(interaction, text="开始爬取",command=crawler).place(x=110,y=160)
textF = tkinter.Label(interaction, text="PS:不选张数默认300").place(x=200,y=165)
interaction.mainloop()


#pyinstaller -F -p C:\Users\admin\PycharmProjects\pythonProject\venv\Lib\site-packages main.py
