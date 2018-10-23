#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: first-test
#     FileName: requestDeo
#         Desc: 
#       Author: Administrator
#        Email: 136665323@qq.com
#     HomePage: dlmdlm.github.io
#       Create: 2018-09-05 17:55
#=============================================================================
"""
import requests
import json

"""
import requests
url="https://api.github.com/user"
data = {
    "user":"dlmdlm",
    "pass":"mf1996106"
}
res = requests.get(url='https://api.github.com/user', data=data)
print res
"""


# 把low代码封装一个函数
class RunMain:
    # python里面的构造方法，这个时候，当我们去实例化这个类的时候，就去自动调用一个方法，即res等于。。。
    def __init__(self, url, method, data=None):
        self.res = self.run_main(url, method, data)  # 这个时候告诉你，你要传一个url，data

    def send_post(self, url, data):  # 发送post请求的一个方法，你只需要告诉我url和data
        res = requests.post(url=url, data=data).json()  # type: object
        # return json.dumps(res)   #json格式化
        return json.dumps(res, indent=2, sort_keys=True)  # json格式化，测试完之后，把结果返回，谁调用我是不管的

    # dump 把返回的结果json格式化，
    # res是返回的数据，如果没有传这个res，则会报错
    # indent的意思是，每个字段的空格是多少
    # 按照key的顺序来 排序
    # print send_post(url,data)  调用函数，传一个url，data进去

    def send_get(self, url, data):
        res = requests.get(url=url, data=data).json()
        return json.dumps(res, indent=2, sort_keys=True)

    def run_main(self, url, method, data=None):  # data可以为空，后面没有data，那不传就可以了
        res = None  # 先给res赋一个空值
        if method == "get":
            # return send_ get(url,data)   #方法有返回值，则需要return打印出来,每判断一次就要return一次，然后改进，用res
            res = self.send_get(url, data)  # 调用也是要用self，对当前对象的调用
        else:
            # return send_post(url,data)
            res = self.send_post(url, data)
        return res


if __name__ == '__main__':
    url = "http://m.imooc.com/passport/user/login"
    data = {
        "username": "13177802129",
        "password": "lovehjd1995",
        "verify": "",
        "referer": "https://m.imooc.com"
    }
run = RunMain(url, "post", data)
print run.res  # 因为是构造函数，已经调用了，那你这里直接调用就可以了 run.res就行，但是是当前类，前面要是self.res=(第33行)
# print run.run_main(url, "post", data)

"""
这个为第4章的内容：讲的封装接口测试的类
    前面讲到了，一个sent_post,一个sent_get请求，如果测试一个接口，知道是有这两个请求方式，然后可以调用这两个方法去测试
    ，但是如果说，我在一个文件里面，我有一个url，有一个get，但是每次都要判断一下，是不是很麻烦。那我想，是不是可以
   通过一种方式，然后把它们封装在一起，到时候就只要调用这一个方法就可以。创建一个run_main函数，同样需要url，data
这两个参数，有了这两个参数后，然后直接告诉你，可以调用那个方法，是get，还是post,但是根据什么来调呢，根据你告诉我的请求
方法类型来调，
"""

"""我现在是个get请求，然后你让我传个参数，那不就是脱了裤子放屁吗？现在我就不想传参数，无论你不写data，还是不放参数data
都是会报错的，那我就想，你的data反正不一定会用，那你的data能不能为空啊，data=none,这样的话，就随你传不传，你传我就用你的，
你不穿，我就默认为空,这个时候要注意，为none时的顺序。
类：接下来，我们用一个类把它们封装起来。建一个RunMain的类，把三个方法都封装起来。那我运行的时候，if__name__,然后run.
在我们的Python里面，用到了类一定要用在各方法里面加个self，否则会报错，当前类，实例化.
进一步完美
构函数：造然后又遇到一个问题，每次去运行的时候都要去实例化一下，实例化后再去调用这个方法.然后就到了构造函数，def__init__
，
改进，构造函数，这个时候，实例化这个类的时候就会自动调用这个方法，即res=self.runmain,，，然后就会告诉你要传URL，method，
data进去然后 def __init__(self, url, method, data=None)  :这个时候把需要的参数传进去，然后把就可以很明确的说
res已经有了，然后数据还是要有的，在if__name__=="__main__"下面，把数据放在运行run=RunMain（）前面了，
放在前面后，要传参数进去 run=RunMain（url，“post”，data）

"""
