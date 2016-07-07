#coding=utf-8
import requests
url = 'http://127.0.0.1:5000'
r = requests.get(url)
print(type(r))
print(dir(r))
print('请求的地址是%s'%r.url)
print('请求的状态码%d'%r.status_code)
print('请求的内容是：%s'%r.content.decode('utf-8'))
