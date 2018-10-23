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

import unittest


class TestDemo(unittest.TestCase):
    def test_01(self):
        print "这是第一个测试用例"

    def test_02(self):
        print "这是第二个测试用例"


if __name__ == '__main__':
    run()
    # unittest.main
    # unittest框架的TestSuite()类是用来创建测试套件的。
    #suite = unittest.TestSuite()
    # addTest()方法是将测试用例添加到测试套件中
    #suite.addTest(TestDemo('test_01'))
    #suite.addTest(TestDemo('test_02'))
    # run()方法是运行测试套件的测试用例，入参为suite测试套件。
    #unittest.TextTestRunner().run(suite)


"""
import unittest
import HTMLTestRunner
from mock import mock
from demo import RunMain
from mock_demo import mock_test


class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = "http://m.imooc.com/passport/user/login"
        data = {
            "username": "13177802129",
            "password": "lovehjd1995",
            "verify": "",
            "referer": "https://m.imooc.com",
            # "status": 10001
        }
        # mock_data = mock.Mock(return_value=data)
        # mock一个方法
        # self.run.run_main = mock_data

        # self.run.run_main = mock.Mock(return_value=data)
        # 调用mock_test（）方法，把模拟的方法名传进去，模拟的是self.run.run_main这个方法，再把其他需要的参数偶都放进去
        # 如果你有很多方法要mock的话，就可以这样写，调用mock_test方法，然后把方法名写进去，
        # res = mock_test(self.run.run_main, data, url, "post", data)
        res = self.run.run_main(url, "post", data)

        self.assertEqual(res["status"], 10001, u"测试成功")
        print "one"

    # @unittest.skip("test_02")
    def test_02(self):
        url = "http://m.imooc.com/passport/user/login"
        data = {
            "username": "13177802129",
            "password": "lovehjd1995",
            "verify": "",
            "referer": "https://m.imooc.com"
        }
        res = self.run.run_main(url, "post", data)
        self.assertEqual(res["status"], 100001, u"测试失败")
        print "two"

    def test_03(self):
        url = "http://m.imooc.com/passport/user/login"
        data = {
            # 主贷人姓名
            "name": "黄黄",
            # 主贷人证件类型
            "certType": "身份证",
            # 主贷人证件号码
            "certNo": "360732199510112578",
            # 主贷人手机号
            "phone": "13166392132",
            # 主贷人婚姻状况
            "maritalStatus": "否",
            # 主贷人附件列表
            "attachlist": {
                "": "",
            },
            # 银行代码
            "bankCode": "23",
            # 购车用途
            "carUsage": "家用",
            # 业务类型
            "businessType": "融资",
            # 车辆构成
            "carStruct": "存量车",
            # 是否双签
            "isDualSign": "否",
            # 是否录配偶信息
            "hasMate": "否",
            # 配偶信息
            "mateInfo": {
                "name": "",
                "certType": "",
                "certNo": "",
                "phone": "",
                "attachList": "",
            },
            # 是否录担保人一信息
            "hasGuar1": "",
            # 担保人一信息
            "guar1Info": {
                "name": "",
                "certType": "",
                "certNo": "",
                "phone": "",
                "relation": "",
                "attachList": "",
            },
            # 是否录担保人二信息
            "hasGuar2": "",
            # 担保人二信息
            "guar2Info": {
                "name": "",
                "certType": "",
                "certNo": "",
                "phone": "",
                "relation": "",
                "attachList": "",
            }

        }
        res = mock_test(self.run.run_main, data, url, "post", data)
        self.assertEqual(res["bankCode"], "23", u"测试失败")
        print "two"


if __name__ == '__main__':
    filepath = "D:/study-python/first-test/report/htmlreport.html"
    fp = file(filepath, "wb")

    # 创建一个容器=放case的集合，命名为suite
    suite = unittest.TestSuite()
    # 创建好后，往容器里面添加testcase
    suite.addTests([TestMethod("test_02")])
    suite.addTests([TestMethod("test_01")])
    suite.addTests([TestMethod("test_03")])
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="this is first report")
    runner.run(suite)
    fp.close()

# 添加好后，可以运行
# unittest.TextTestRunner().run(suite)
# unittest.main()
"""