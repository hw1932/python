#coding=utf-8
from selenium import webdriver

user = '947412461@qq.com'
pwd = 'a123456'

#登陆
def login(driver):
	#driver.find_element_by_id("u").clear()
	driver.find_element_by_id("txtLogname").send_keys(user)
	#driver.find_element_by_id("p").clear()
	driver.find_element_by_id("txtPass").send_keys(pwd)
	driver.find_element_by_id("btnLogin").click()
	
#退出
def logout(driver):
	driver.find_element_by_link_text("退出").click()
	driver.quit()
	
driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("http://www.pyc.com.cn/login.aspx")
login(driver) #调用登陆模块
#收信、写信、删除信件等操作
logout(driver) #调用退出模块
