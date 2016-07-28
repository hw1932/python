#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
#下面的例子中，百度输入框的定位 id=kw22 是有误的，那么在超出 10 秒后将抛出异常。
input_ = driver.find_element_by_id("kw22")
input_.send_keys('selenium')
driver.quit()
'''
implicitly_wait()默认参数的单位为秒，本例implicitly_wait_baidu中设置等待时长为 10 秒，
首先这 10 秒并非一个固定的等待时间，它并不影响脚本的执行速度。
其次，它并不真对页面上的某一元素进行等待，当脚本执行到某个元素定位时，如果元素可定位那么继续执行，如果元素定位不到，那么它将以轮询的方式不断的判断元素是否被定位到，假设在第6秒钟定位到元素则继续执行。直接超出设置时长（10 秒）还没定位到元素则抛出异常。
'''