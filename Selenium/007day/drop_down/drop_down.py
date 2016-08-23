#-*-coding=utf-8
from selenium import webdriver
import os,time

driver= webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('drop_down.html')
driver.get(file_path)
time.sleep(2)

#方法一，先定位到下拉框
m=driver.find_element_by_id("ShippingMethod")
#再点击下拉框下的选项
m.find_element_by_xpath("//option[@value='10.69']").click()

#方法二，直接定位到指定项
#driver.find_element_by_xpath('//option[@value = "9.03"]').click()

time.sleep(5)
driver.quit()

#方法三，利用键盘事件切换下拉列表
'''
#coding:utf-8
#引用模块
from selenium.webdriver.common.keys import Keys
from selenium  import webdriver
import os

#初始化
browser=webdriver.Firefox()
file_path='file:///'+os.path.abspath('drop_down.html')
browser.get(file_path)

#在选择框中定位元素'USPS Priority Mail ==> $7.45'并在选择框显示
browser.find_element_by_id('ShippingMethod').click()
browser.find_element_by_id('ShippingMethod').send_keys(Keys.UP)
browser.find_element_by_id('ShippingMethod').send_keys(Keys.ENTER)

time.sleep(5)
browser.close()
'''