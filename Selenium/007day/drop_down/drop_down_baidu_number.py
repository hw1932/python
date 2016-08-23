#coding:utf-8
'''
进入百度搜索设置页面，设置每页显示数量为50条，保存后进行一次搜索，查看显示结果是否为50条

'''

#导入相关模块
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

#通过火狐浏览器访问百度地址
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')

#通过关键字“设置”将鼠标移动到“设置”上
webdriver.ActionChains(driver).move_to_element(driver.find_element_by_link_text(u'设置')).perform()

#定位到“搜索设置”并点击
WebDriverWait(driver,5).until(lambda driver:driver.find_element_by_link_text(u'搜索设置')).click()

#设置每页显示数量为50条，然后保存设置
WebDriverWait(driver,5).until(lambda driver:driver.find_element_by_xpath('//option[@value = "50"]')).click()
driver.find_element_by_link_text(u'保存设置').click()
driver.find_element_by_link_text(u'保存设置').click()
#点击弹出窗
driver.switch_to_alert().accept()

#保存设置后返回首页进行搜索
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()

for n in range(0,100,5):
    js='document.documentElement.scrollTop=document.documentElement.scrollHeight*%s'%(n/100.0)
    driver.execute_script(js)
lists=driver.find_elements_by_xpath('//div/h3/a[1]')
print ('当前页面搜索结果数量为 %d') %len(lists)

time.sleep(5)
driver.close()
