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
#       Create: 2018-09-06 17:20
#=============================================================================
"""

import requests
import json


class RunMain:  # 三个方法都发放进类里面

    # """def __init__(self,url,method,data=None):
    #     self.res = self.run_main(url,method,data)"""

    def send_post(self, url, data):
        res = requests.post(url=url, data=data)
        # return json.dumps(res, indent=2, sort_keys=True)
        return res

    def send_get(self, url, data):
        res = requests.get(url=url, data=data).json()
        # return json.dumps(res, indent=2, sort_keys=True)
        return res

    def run_main(self, url, method, data=None):  # data可以为空，后面没有data，那不传就可以了
        res = None  # 先给res赋一个空值
        if method == "get":
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res  # 执行完后返回


if __name__ == "__main__":
    run = RunMain()
    url = "http://m.imooc.com/passport/user/login"
    data = {
        "username": "13100000000",
        "password": "hhhhhhh",
        "verify": "",
        "referer": "https://m.imooc.com"
    }
    print run.run_main(url, "post", data)  # 运行下这个程序
