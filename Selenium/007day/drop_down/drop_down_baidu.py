#-*-coding=utf-8
from selenium import webdriver
import os,time
driver= webdriver.Firefox()
driver.get("http://www.baidu.com")
#������������ҳ
#driver.find_element_by_link_text("��������").click()
driver.find_element_by_css_selector('#wrapper > div.bdpfmenu > a.setpref').click()

#����ÿҳ�������Ϊ100��
m=driver.find_element_by_name("NR")
m.find_element_by_xpath("//*[@id='nr']/option[3]").click()
time.sleep(2)
#�������õ���Ϣ
#driver.find_element_by_xpath("//input[@value='��������']").click()
driver.find_element_by_css_selector('#gxszButton > a.prefpanelgo').click()
time.sleep(2)
driver.switch_to_alert().accept()
#��ת���ٶ���ҳ�󣬽���������һҳӦ����ʾ100�������
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.quit()