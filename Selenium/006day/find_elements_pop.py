#coding=utf-8
from selenium import webdriver
import time
import os
dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('checkbox.html')
dr.get(file_path)
# ѡ�����е� checkbox ��ȫ������
checkboxes = dr.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
	checkbox.click()
time.sleep(2)
# ��ҳ�������1�� checkbox �Ĺ���ȥ��
dr.find_elements_by_css_selector('input[type=checkbox]').pop().click()
time.sleep(2)
dr.quit()