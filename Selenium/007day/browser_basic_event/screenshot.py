#coding=utf-8
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.baidu.com')

try:
	driver.find_element_by_id('kw_wrong').send_key('selenium')
	driver.find_element_by_id('su').click()

except :
	driver.get_screenshot_as_file("D:\\baidu_error.jpg")
	driver.quit()