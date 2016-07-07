#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.base_url = 'http://www.baidu.com/'
        self.verficationErrors = []
        self.accept_next_alert = True

    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url+'/')
        try:
            #kwddd do not exist
            driver.find_element_by_id('kwdddd').send_keys('selenium')
        except:
            #if not found, take picture
            driver.get_screenshot_as_file('e:\\abc\\123\\kw.png')

        driver.find_element_by_id('su').click()
        time.sleep(2)
        driver.close()

    def test_baidu_set(self):
        pass

    def test_baidu_xxx(self):
        pass

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verficationErrors)

def suite():#构造测试集

    return suite
if __name__ == '__main__':
    #unittest.main()
    '''
    PyUnit 模块中定义了一个名为 main 的全局方法，使用它可以很方便地将一个单元测
试模块变成可以直接运行的测试脚本，main()方法使用 TestLoader 类来搜索所有包含
在该模块中的测试方法，并自动执行它们。如果 Python 程序员能够按照约定（以 test
开头）来命名所有的测试方法，那就只需要使用unittest.main()即可
    '''
    #容器可以在全局中定义suite()方法，也可以像这样在if main后面定义
    suite = unittest.TestSuite()
    #逐个添加测试用例到suite容器
    suite.addTest(Baidu('test_baidu_search'))
    suite.addTest(Baidu('test_baidu_set'))
    suite.addTest(Baidu('test_baidu_xxx'))

    runner = unittest.TextTestRunner()
    runner.run(suite)

