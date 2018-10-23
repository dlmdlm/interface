#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: first-test
#     FileName: haha
#         Desc: 
#       Author: Administrator
#        Email: 136665323@qq.com
#     HomePage: dlmdlm.github.io
#       Create: 2018-09-07 13:49
#=============================================================================
"""
import unittest
from unittest import defaultTestLoader
import HTMLTestRunner
import sys
sys.path.append('../interface')
from mock import mock
from demo import RunMain
from mock_demo import mock_test

test_dir = '../interface'
testsuit = defaultTestLoader.discover(test_dir, pattern="*_One.py")

if __name__ == '__main__':
    filepath = "F:/study-python/unittest-zeroUpKJ/report/htmlreport.html"
    fp = file(filepath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="this is first report")
    runner.run(testsuit)
    fp.close()

# 添加好后，可以运行
# unittest.TextTestRunner().run(suite)
# unittest.main()
