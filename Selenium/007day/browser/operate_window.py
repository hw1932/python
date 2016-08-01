#coding=utf-8
from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get("https://www.baidu.com")
print ("浏览器最大化")
browser.maximize_window() #将浏览器最大化显示
time.sleep(2)
print ("设置浏览器宽480、高800显示")
browser.set_window_size(480, 800)
time.sleep(3)

#访问百度首页
first_url= 'https://www.baidu.com'
print ("the first site we access ->%s" %(first_url))
browser.get(first_url)
time.sleep(2)
#访问百度云盘页面
second_url='http://pan.baidu.com'
print ("the second site we access ->%s" %(second_url))
browser.get(second_url)
time.sleep(2)

#返回（后退）到百度首页
print ("back to %s "%(first_url))
browser.back()
time.sleep(1)
#前进到云盘页
print ("forward to %s"%(second_url))
browser.forward()
time.sleep(2)
browser.quit()