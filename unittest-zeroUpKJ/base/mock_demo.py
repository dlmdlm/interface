#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: first-test
#     FileName: mock_demo
#         Desc: 
#       Author: Administrator
#        Email: 136665323@qq.com
#     HomePage: dlmdlm.github.io
#       Create: 2018-09-17 16:37
#=============================================================================
"""
from mock import mock


def mock_test(func, request_data, url, method, response_data):
    """ 模拟mock封装，那其他地方就可以调用了"""
    # mock这个语句的时候要有一个返回数据response_data"""
    mock_method = mock.Mock(return_value=response_data)
    # 给他一个返回值，然后去执行他，需要传url，method，request_data
    res = mock_method(url, method, request_data)
    # 然后把res返回出去
    return res
