#coding=utf-8

import unittest,doctest
from . import test_baidu #导入待测试的文件
import HTMLTestRunner

suite = doctest.DocTestSuite()
#罗列要执行的文件
suite.addTest(unittest.makeSuite(test_baidu))

unittest.TextTestRunner(verbosite=2).run(suite)