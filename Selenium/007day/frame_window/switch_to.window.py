#coding=utf-8
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

#获得百度搜索窗口句柄
sreach_windows = driver.current_window_handle
time.sleep(2)
driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text("立即注册").click()

#获得当前所有打开的窗口的句柄
time.sleep(2)
all_handles = driver.window_handles
print(type(all_handles),len(all_handles))
#进入注册窗口
for handle in all_handles:
	time.sleep(2)
	print('the first for')
	if handle != sreach_windows:
		driver.switch_to.window(handle)
		print ('now register window!')
		driver.find_element_by_id("TANGRAM__PSP_3__phone").send_keys('username')
		driver.find_element_by_id('TANGRAM__PSP_3__password').send_keys('password')

#进入搜索窗口
for handle in all_handles:
	time.sleep(2)
	print('the second for')
	if handle == sreach_windows:
		time.sleep(2)
		driver.switch_to.window(handle)
		print ('now sreach window!')
		driver.find_element_by_id('TANGRAM__PSP_2__closeBtn').click()
		driver.find_element_by_id("kw").send_keys("selenium")
		driver.find_element_by_id("su").click()
		time.sleep(2)
to_be_end = input('输入任意键结束')
driver.quit()
