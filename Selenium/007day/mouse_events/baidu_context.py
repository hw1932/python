#coding:utf-8
from selenium import webdriver
#引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
#引入条件等待
from selenium.webdriver.support import expected_conditions as EC
#引入显式等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://yun.baidu.com")

#登录
driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('3000huangwei')
driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys('a123123')
driver.find_element_by_id('TANGRAM__PSP_4__submit').click()

#判断是否需要验证码
try:
    verifyCode = WebDriverWait(driver,2,0.5).until(EC.presence_of_element_located((By.ID,"TANGRAM__PSP_4__verifyCode")))
    if not verifyCode:
        pass
    else:
        codeinput = input(u'请输入验证码：')
        verifyCode.send_keys(codeinput)
        driver.find_element_by_id('TANGRAM__PSP_4__submit').click()
except Exception as e:
     pass

#跳转到网盘
WebDriverWait(driver,2,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#aside > ul.app-entry > li:nth-child(1) > a"))).click()
#刷新浏览器
driver.refresh()
#定位到要右击的元素
right_click = driver.find_element_by_xpath('//*[@id="layoutMain"]/div[2]/div[3]/div/div[1]/dd[3]/span')

#对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(right_click).perform()
#观察页面变化
driver.implicitly_wait(2)
#关闭浏览器退出
driver.close()

'''
from selenium.webdriver import ActionChains
对于 ActionChains 类下面的方法，在使用之前需要先将模块导入。
ActionChains(driver)
调用 ActionChains()方法，在使用将浏览器驱动 driver 作为参数传入。
context_click(right_click)
context_click()方法用于模拟鼠标右键事件，在调用时需要传入右键的元素。
perform()
执行所有 ActionChains 中存储的行为，可以理解成是对整个操作事件的提交动作
'''