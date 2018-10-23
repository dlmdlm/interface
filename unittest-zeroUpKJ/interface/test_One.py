#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: first-test
#     FileName: test_One
#         Desc: 
#       Author: Administrator
#        Email: 136665323@qq.com
#     HomePage: dlmdlm.github.io
#       Create: 2018-09-19 16:24
#=============================================================================
"""
from mock import mock
from base import demo
from base import mock_demo

import unittest
import time, sys

sys.path.append("../demo")


class TestOne(unittest.TestCase):
    """the first test"""

    def setUp(self):
        self.run = demo.RunMain()

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

    @unittest.skip("test_02")
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
            "attachlist": [],
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
        res = mock_demo.mock_test(self.run.run_main, data, url, "post", data)
        self.assertEqual(res["bankCode"], "23", u"测试失败")
        print "two"

    def test_04(self):
        url = "http://piccimg.chedai0.com/Guarantee/Order/save"
        data = {
            "seat": [
                {
                    "o_back": "宁波东海银行",
                    "o_back_id": "27"
                },
                {
                    "d_text": "存量车",
                    "d_id": "3405",
                    "cr_constitute": "存量车",
                    "cr_age": "12",
                    "loan_use": "个人家庭综合消费",
                    "cr_loan": "66666"
                },
                {
                    "cm_type": "购车人",
                    "o_vip_name": "邓丽梅",
                    "o_vip_card": "360732199310062621",
                    "o_vip_tel": "13177802129",
                    "o_vip_marriagestatus": "未婚单身",
                    "cm_card_no": "6217002020021597265",
                    "nationality": "汉族",
                    "cert_start_date": "2013-09-03",
                    "cert_start_end": "2023-09-03",
                    "nationality_code": "01",
                    "card_name": [
                        "身份证正面",
                        "身份证反面",
                        "客户正脸照"
                    ],
                    "card_url": [
                        "Uploads/2018/09/153745617308982500.jpg",
                        "Uploads/2018/09/153745617565301000.jpg",
                        "Uploads/2018/09/153745617894432800.jpg"
                    ],
                    "card_id": [
                        "12378",
                        "12379",
                        "12380"
                    ]
                },
                {
                    "cm_type": "配偶",
                    "o_vip_name": "",
                    "o_vip_card": "",
                    "o_vip_tel": "",
                    "cert_start_date": "",
                    "cert_start_end": "",
                    "card_name": [
                        "身份证正面",
                        "身份证反面"
                    ],
                    "card_url": [
                        "",
                        ""
                    ],
                    "card_id": [
                        "",
                        ""
                    ]
                }
            ],
            "o_type": "",
            "number": "",
            "rb_require": 1
        }
        res = mock_demo.mock_test(self.run.run_main, data, url, "post", data)
        self.assertEqual(res["rb_require"], 1, u"测试失败")
        print "two"


if __name__ == '__main__':
    unittest.main()
