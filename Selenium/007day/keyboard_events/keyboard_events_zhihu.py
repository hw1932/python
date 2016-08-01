#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #需要引入 keys 包
import os,time
driver = webdriver.Firefox()
driver.get("https://www.zhihu.com/#signin")
time.sleep(3)
driver.maximize_window() # 浏览器全屏显示

username = 'account'
password = 'password'
account = '15538226525'
pwd = 'a123123'

driver.find_element_by_name(username).clear()
driver.find_element_by_name(username).send_keys(account)

#tab 切换到下一个输入框，这里从登录名切换到密码
driver.find_element_by_name(username).send_keys(Keys.TAB)
time.sleep(2)
driver.find_element_by_name(password).send_keys(pwd)
time.sleep(3)
#通过定位密码框，enter（回车）来代替登陆按钮
driver.find_element_by_name(password).send_keys(Keys.ENTER)
time.sleep(3)

driver.quit()