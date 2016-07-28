#coding=utf-8
from selenium import webdriver
import os,time
driver = webdriver.Firefox()
#脚本要与 upload_file.html 同一目录
file_path = 'file:///' + os.path.abspath('upload.html')
driver.get(file_path)
#定位上传按钮，添加本地文件
input('---------')
driver.find_element_by_name("file").send_keys(file_path)
time.sleep(2)
input('---------')
driver.quit()