#coding=utf-8
from selenium import webdriver
import os,time
driver = webdriver.Firefox()
driver.get("http://m.mail.10086.cn")
driver.implicitly_wait(30)
#登陆，输入自己的帐号
driver.find_element_by_id("ur").send_keys("手机号")
driver.find_element_by_id("pw").send_keys("密码")
driver.find_element_by_class_name("loading_btn").click()
time.sleep(3)
#进入139网盘模块
driver.find_element_by_xpath("/html/body/div[3]/a[9]/span[2]").click()
time.sleep(3)
#定义上传文件位置
file_path = 'file:///' + os.path.abspath('upload.html')
#上传文件
driver.find_element_by_id("id_file").send_keys(file_path)
time.sleep(5)
driver.quit()