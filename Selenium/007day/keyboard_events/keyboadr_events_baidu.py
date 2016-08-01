#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #需要引入 keys 包
import os,time
driver = webdriver.Firefox()
driver.get("https://passport.baidu.com")
time.sleep(3)
driver.maximize_window() # 浏览器全屏显示

username = 'TANGRAM__PSP_3__userName'
password = 'TANGRAM__PSP_3__password'

driver.find_element_by_id(username).clear()
driver.find_element_by_id(username).send_keys("3000huangwei")
#tab 切换到下一个输入框，这里从登录名切换到密码
driver.find_element_by_id(username).send_keys(Keys.TAB)
time.sleep(3)
driver.find_element_by_id(password).send_keys('a123123')
#通过定位密码框，enter（回车）来代替登陆按钮
driver.find_element_by_id(password).send_keys(Keys.ENTER)
'''
#也可定位登陆按钮，通过 enter（回车）代替 click()
driver.find_element_by_id("login").send_keys(Keys.ENTER)
'''
time.sleep(3)
driver.quit()