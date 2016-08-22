#!/usr/bin/Python3.5.0
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
import os
import time

driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath('drag_drop.html')
driver.get(file_path)

source = driver.find_element(By.ID,"Source")
target = driver.find_element(By.ID,"Target")
ActionChains(driver).drag_and_drop(source,target).perform() 
time.sleep(1)
