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
import HTMLTestRunner
from demo import RunMain
from urllib import unquote
from mock import mock
from mock_demo import mock_test


class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = "http://chedai.picc2.dev.com:88/api/test/getEncryptRequestData:"
        header = {
            "requestSeqNo": "Picc1201254715345799565681",
            "partnerCode": "09999999",
            "interfaceCode": "GetPolicyDetail",
            "interfaceVersion": "v1",
        }
        data = {
            "policyNumber": "PUBA201633020000000066"  # 保单号
        }
        encrypt_data = self.run.run_main(url, "post", data={'header': header, 'data': data})
        print unquote(encrypt_data.text)    # 返回数据Unicode处理
        return encrypt_data    # 把返回数据返回出去

    # @unittest.skip("test_02")
    def test_02(self):
        encrypt_data = self.test_01()     # 接受test_01的数据
        url = "http://chedai.picc2.dev.com:88/api/jobs/channel"
        res = self.run.run_main(url, "post", encrypt_data)
        print res.text
        return res

    def test_03(self):
        data = self.test_02()     # 接受test_01的数据
        url = "http://chedai.picc2.dev.com:88/api/test/getDecryptResponseData"
        res = self.run.run_main(url, "post", data)
        print res.text


if __name__ == '__main__':
    filepath = "F:/study-python/unittest-zeroKJ/report/htmlreport.html"
    fp = file(filepath, "wb")

    # 创建一个容器=放case的集合，命名为suite
    suite = unittest.TestSuite()
    # 创建好后，往容器里面添加testcase
    suite.addTests([TestMethod("test_01")])
    suite.addTests([TestMethod("test_02")])
    suite.addTests([TestMethod("test_03")])
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="this is first report")
    runner.run(suite)
    fp.close()

# 添加好后，可以运行
# unittest.TextTestRunner().run(suite)
# unittest.main()
