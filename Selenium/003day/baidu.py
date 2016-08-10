# coding = utf-8
from selenium import webdriver
import time

browser = webdriver.Firefox()
#browser = webdriver.Chrome()
browser.get("http://www.baidu.com")

#browser.find_element_by_xpath("//span[@class='bg s_ipt_wr']/input[@class='s_ipt']").send_keys('selenium')
#browser.find_element_by_id("kw" ).send_keys( "selenium")
#browser.find_element_by_xpath("//div[@id='lg']/img")
browser.find_element_by_xpath("//form[@id='form']/span/span").click()
#browser.find_element_by_id("su").click()
#browser.find_element_by_id("kw").submit()
time.sleep(3)
browser.close()