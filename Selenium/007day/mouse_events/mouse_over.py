#coding:utf-8
#-*- coding: utf-8 -*-
import time
from selenium import webdriver
#引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
#定位到要悬停的元素
#above = driver.find_element_by_css_selector("#s_usersetting_top > span")
#above = driver.find_element_by_xpath('//*[@id="s_usersetting_top"]/span')
#above = driver.find_element_by_css_selector("span.setting-text")
#above = driver.find_element_by_css_selector('html body div#wrapper div#head div.head_wrapper div.bdbri.bdbriimg div.bdmainlink div.bdbriimgtitle')
#above = driver.find_element_by_xpath('//a[@name="tj_settingicon"]/span')
above = driver.find_element_by_link_text('更多产品')
#对定位到的元素执行悬停操作
ActionChains(driver).move_to_element(above).perform()
time.sleep(3)