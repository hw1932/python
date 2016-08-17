#coding=utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.pyc.com.cn/login.aspx")

class Account(object):
"""docstring for Account"""
	def __init__(self,username ='', password = ''):
		self.username = username
		self.password = password
		
def do_login_as(user_info):
	driver.find_element_by_id("idInput").clear()
	driver.find_element_by_id("idInput").send_keys(user_info.username)
	driver.find_element_by_id("pwdInput").clear()
	driver.find_element_by_id("pwdInput").send_keys(user_info.password)
	driver.find_element_by_id("loginBtn").click()

file_info = open('pyc_login_out_dataDrive_info.txt','r')
values = file_info.readlines()
file_info.close()
	 
#实例化登陆信息
admin = Account(username='admin',password='123')
guset = Account(username='guset',password='321')
#调用登陆函数
do_login_as(admin)
do_login_as(guset)