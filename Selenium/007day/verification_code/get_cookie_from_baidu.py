#coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Firefox() 
#访问 xx 网站
driver.get("https://www.baidu.com")
driver.find_element_by_link_text('登录').click()
time.sleep(2)
user = '3000huangwei'
pwd = 'a123123'

driver.find_element_by_id('TANGRAM__PSP_8__userName').send_keys(user)
driver.find_element_by_id('TANGRAM__PSP_8__password').send_keys(pwd)
driver.find_element_by_id('TANGRAM__PSP_8__memberPass').click()
driver.find_element_by_id('TANGRAM__PSP_8__submit').click()
time.sleep(2)

# 获得 cookie 信息
cookie= driver.get_cookies()
#将获得 cookie 的信息打印
print (cookie)
'''
#将用户名密码写入浏览器 cookie
driver.add_cookie({'name':'Login_UserNumber', 'value':user})
driver.add_cookie({'name':'Login_Passwd', 'value':pwd})
#再次访问 xx 网站，将会自动登录
driver.get("http://www.xx.cn/")
'''
time.sleep(3)
driver.quit()