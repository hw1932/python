﻿#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
dr = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('level_locate.html')
dr.get(file_path)
#点击 Link1链接（弹出下拉列表）
dr.find_element_by_link_text('Link1').click()
#找到 id 为 dropdown1的父元素
WebDriverWait(dr, 10).until(lambda the_driver:the_driver.find_element_by_id('drop4').is_displayed())
#在父亲元件下找到 link 为 Action 的子元素
menu = dr.find_element_by_id('drop4').find_element_by_link_text('Action')
#鼠标定位到子元素上
webdriver.ActionChains(dr).move_to_element(menu).perform()
time.sleep(2)
dr.quit()