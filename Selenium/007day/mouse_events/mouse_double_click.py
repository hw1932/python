#coding:utf-8
import os
import time
from selenium import webdriver
#引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)

#定位到要悬停的元素
double_click = driver.find_element_by_id("c1")
#对定位到的元素执行双击操作
ActionChains(driver).double_click(double_click).perform()
input('注意看是否是双击')
driver.close()