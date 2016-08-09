# coding = utf-8
from selenium import webdriver
import time

#browser = webdriver.Firefox()
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw" ).send_keys( "selenium")
browser.find_element_by_id("su").click()
#browser.find_element_by_id("kw").submit()
time.sleep(3)
browser.quit()