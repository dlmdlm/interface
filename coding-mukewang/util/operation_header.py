# coding:utf-8
import requests
import json
from operation_json import OperetionJson


class OperationHeader:

    def __init__(self, response):
        self.response = json.loads(response)

    def get_response_url(self):
        """
        获取登录返回的token的url
        """
        url = self.response['data']['url'][0]
        return url

    def get_cookie(self):
        """
        获取cookie的jar文件
        """
        url = self.get_response_url() + "&callback=jQuery21008240514814031887_1508666806688&_=1508666806689"
        cookie = requests.get(url).cookies
        return cookie

    def write_cookie(self):
        """ 定义一个write_cookie的方法"""
        # 执行get_cookie()方法
        c = self.get_cookie()
        cookie = requests.utils.dict_from_cookiejar(c)
        op_json = OperetionJson()
        op_json.write_data(cookie)


def test():
    # 接口地址
    url = "http://m.imooc.com/passport/user/login"
    # 去请求接口需要的参数
    data = {
        "username": "13177802129",
        "password": "lovehjd1995",
        "verify": "",
        "referer": "https://m.imooc.com"
    }
    # 发送请求，请求结果赋给response
    response = requests.post(url, data=data, timeout=3)
    # 把结果的中的数据以json格式拿出来
    result = response.json()
    # 把json格式转出json字符串，dump方法，
    res = json.dumps(result)
    # 实例化对象，把一个类实例化，然后赋值给一个变量
    op_header = OperationHeader(res)
    op_header.write_cookie()


if __name__ == '__main__':
    test()
