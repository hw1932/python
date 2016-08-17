#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os

#初始化
file_path = 'file:///' + os.path.abspath('drag_drop_0817.html')
d = webdriver.Firefox()
d.get(file_path)

#定位元素
source_id = '1'
target_id = '3'
try:
    source = d.find_element_by_id(source_id)
    target = d.find_element_by_id(target_id)
    #source = d.find_element_by_link_text('Python')
    #target = d.find_element_by_link_text('UTF-8')
except:#定位失败则退出浏览器，并打印失败消息
    print('fail to locate')
    d.close()
else:#定位成功则继续下一步，并打印成功消息
    print('successfully located')
        


#拖动
ActionChains(d).drag_and_drop(source,target).perform()
input('after check out the web page,please press any keys to close the driver')
d.close()