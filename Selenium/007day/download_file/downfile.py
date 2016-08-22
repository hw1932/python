#coding=utf-8
from selenium import webdriver
import os

#为了让 FireFox 让浏览器能实现文件的载，需要通过 FirefoxProfile() 对其参数做一个设置
fp = webdriver.FirefoxProfile()
#设置成 0 代表下载到浏览器默认下载路径；设置成 2 则可以保存到指定目录。
fp.set_preference("browser.download.folderList",2)
#是否显示开始，Ture 为显示，Flase 为不显示。
fp.set_preference("browser.download.manager.showWhenStarting",False)
#用于指定你所下载文件的目录。os.getcwd() 该函数不需要传递参数，用于返回当前的目录。
fp.set_preference("browser.download.dir", os.getcwd())
#指定要下载页面的 Content-type 值，“application/octet-stream”为文件的类型。HTTP Content-type 常用对照表：http://tool.oschina.net/commons
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream") #下载文件的类型

driver = webdriver.Firefox(firefox_profile=fp)
driver.get("http://pypi.Python.org/pypi/selenium")
driver.find_element_by_partial_link_text("selenium-3.0.0b2-py2.py3-none-any.whl").click()