#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: first-test
#     FileName: test
#         Desc: 
#       Author: Administrator
#        Email: 136665323@qq.com
#     HomePage: dlmdlm.github.io
#       Create: 2018-09-07 13:47
#=============================================================================
"""
# import unittest
import unittest

"""class TestSome(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        assert 1 == 1
        print 1111111

    def test_2(self):
        assert 1 == 1
        print 2222


if __name__ == '__main__':
    unittest.main()

    # case1 = unittest.TestLoader().loadTestsFromTestCase(TestSome)
    # suite = unittest.TestSuite([case1, ])
    # unittest.TextTestRunner(verbosity=3).run(suite)
"""


class TestDemo(unittest.TestCase):
    def test_01(self):
        print "这是第一个测试用例"

    def test_02(self):
        print "这是第二个测试用例"


if __name__ == '__main__':
    run()
    # unittest.main
    # unittest框架的TestSuite()类是用来创建测试套件的。
    # suite = unittest.TestSuite()
    # addTest()方法是将测试用例添加到测试套件中
    # suite.addTest(TestDemo('test_01'))
    # suite.addTest(TestDemo('test_02'))
    # run()方法是运行测试套件的测试用例，入参为suite测试套件。
    # unittest.TextTestRunner().run(suite)
