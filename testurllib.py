import urllib.request
#httpbin.org 用于测试的网站

#get方式获取网页内容
response = urllib.request.urlopen("http://www.baidu.com")   #获取网页内容封装体
print(response.read().decode('utf-8'))


'''#post方式获取，可以模拟登录
import urllib.parse
data=bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8") #post封装发送信息
response = urllib.request.urlopen("http://httpbin.org/post",data= data)
print(response.read().decode('utf-8'))
'''
'''
#超时处理
try:
    response = urllib.request.urlopen("https://www.baidu.com",timeout=10)   #timeout处理超时
    print(response.status)  # 状态码
    print(response.getheaders())
    print(response.getheader("server"))
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    print("timeout")
'''

'''
url = "https://www.baidu.com"
data=bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"}
req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
'''

