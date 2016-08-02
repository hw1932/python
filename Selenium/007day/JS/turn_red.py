#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.zhihu.com/#signin")

#给用户名的输入框标红
js='var q=document.querySelector(".email input");q.style.border=\"1px solid red\";'

#调用 js
driver.execute_script(js)
time.sleep(3)

#登录
driver.find_element_by_name("account").send_keys("3000huangwei")
driver.find_element_by_name("password").send_keys("a123123")
driver.find_element_by_link_text("登录").click()
time.sleep(3)

driver.quit()