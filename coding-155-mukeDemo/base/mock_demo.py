# coding:utf-8
from mock import mock


# 模拟mock 封装
def mock_test(request_data, url, method, response_data):
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(url, method, request_data)
    return res
