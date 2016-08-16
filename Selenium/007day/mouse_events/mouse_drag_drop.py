from selenium import webdriver
#引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
#引入条件等待
from selenium.webdriver.support import expected_conditions as EC
#引入显式等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#初始化
driver = webdriver.Firefox()
driver.get('https://pan.baidu.com')
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
        codeinput = str(input('请输入验证码：'))
        verifyCode.send_keys(codeinput)
        driver.find_element_by_id('TANGRAM__PSP_4__submit').click()
except Exception as e:
     pass

#跳转到网盘
#WebDriverWait(driver,2,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#aside > ul.app-entry > li:nth-child(1) > a"))).click()

#刷新浏览器
driver.refresh()

#定位元素的源位置
#element = WebDriverWait(driver,2,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#aside > ul.app-entry > li:nth-child(1) > a")))
element = driver.find_element_by_css_selector("#layoutMain > div.module-list > div.list-view-container > div > div.list-view > dd.g-clearfix.list-view-item.open-enable.hover-item > div.file-name > div.text > a")
#定位元素要移动到的目标位置
target = driver.find_element_by_css_selector("#layoutMain > div.module-list > div.list-view-container > div > div.list-view > dd:nth-child(2) > div.file-name > div.text > a")
#执行元素的拖放操作
ActionChains(driver).drag_and_drop(element,target).perform()

#观察页面变化

#关闭浏览器退出
driver.close()