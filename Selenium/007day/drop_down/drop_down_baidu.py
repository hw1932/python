#-*-coding=utf-8
from selenium import webdriver
import os,time
driver= webdriver.Firefox()
driver.get("http://www.baidu.com")
#进入搜索设置页
#driver.find_element_by_link_text("搜索设置").click()
driver.find_element_by_css_selector('#wrapper > div.bdpfmenu > a.setpref').click()

#设置每页搜索结果为100条
m=driver.find_element_by_name("NR")
m.find_element_by_xpath("//*[@id='nr']/option[3]").click()
time.sleep(2)
#保存设置的信息
#driver.find_element_by_xpath("//input[@value='保存设置']").click()
driver.find_element_by_css_selector('#gxszButton > a.prefpanelgo').click()
time.sleep(2)
driver.switch_to_alert().accept()
#跳转到百度首页后，进行搜索表（一页应该显示100条结果）
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.quit()