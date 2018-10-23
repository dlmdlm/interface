#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: mukeStudy_practice
#     FileName: run_test
#         Desc: 
#       Author: Administrator
#        Email: 136665323@qq.com
#     HomePage: dlmdlm.github.io
#       Create: 2018-10-11 19:24
#=============================================================================
"""
"""
主程序的的入口 

首先这还是个主程序的入口，同样的还是一个class，这次肯定需要构造函数，为什么呢，因为我们为了方便，我们在测试的时候，要调用
base下面的runmethod。所以，我们先把runmethond先导入进来from base import runmethod。然后把RunTest实例化，
self.run_method = RunMethod(),我们的这个方法已经有了，有了后，我们要思考下，我们要拿到数据，拿到数据，我们是不是要调用data
下面的get_data方法，因为我们的所有数据都是在里面拿的，那我们是不是也要导进来:from data.get_data import get_data
然后在下面我们也把GetData拿进去self.data = GetData(),那我们现在这两个对象都有了，那我们是不是只需要执行主程序的入口就可以了
然后只需要做一件事就行了。要怎么干呢，首先我们说过，我要知道你这个case要执行多少行，那我是不是要根据拿到excel的行数来进行判断
那我们首先要干的一件事就是：在一个方法里面， def go_on_run(self):拿到我们所有的行数self.data.get_case_lines()，
赋值一下，那我们是不是可以去循环他了啊，for i in range(1,rows_count),eg:我们拿到了10行，那执行是不是0,1,2,3,4.。。。
但是，我们拿到的excel行数，第一行是不是不用执行的啊，那怎么来控制呢，我们用range函数来控制，那就是从第一行开始执行了
那我们现在拿到了一行数，那我们接下类是不是，去选url，是否执行，请求数据，等等这些参数，只有拿到了后，才能根据是否执行去做判断
然后去拼接数据，
那我们现在直接去拿数据，
            # 需要传一个行号进去，那这里行号是不是就是i，这个时候url就有了，然后把method也传进去
            url = self.data.get_url(i)
            # 已经有method，那我们接下来是不是判断，这个东西他到底要不要执行
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i),然后在拿到我们的请求数据，mushishi老师说data = self.data.get_request_data()
这里面有个坑，但是还是先这样来弄,因为只有先安思路来，才知道哪里会有错，因为我们会发现，self.data.get_request_data()获取
到的是请求数据，我们还要去json文件里面取对应的数据，所以我们不能调用这个方法，而是要调用self.data.get_data_for_json(i)
这样数据才有了，那现在数据就有了，现在我就可以去判断了，那我们是不是可以拿来判断了，如果说is_run返回的是true，那就让你去
（执行我们下面的方法，方法就是：）
我们就去执行run_method里面run_main,然后把需要的数据填进去就可以了。然后把结果返回出去，res
"""
from base.runmethod import RunMethod
from data.get_data import GetData


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()

    def go_on_run(self):
        # 获取我们excel的所有行数，就是我们的case个数
        res = None
        rows_count = self.data.get_case_lines()  # case个数，我们拿到的行数
        for i in range(1, rows_count):  # 因为第一行是要排除的，是头，所以从第二行开始
            # 需要传一个行号进去，那这里行号是不是就是i，传进去就可以了，这个时候url就有了，然后把method也传进去
            url = self.data.get_url(i)
            # 已经有method，那我们接下来是不是判断，这个东西他到底要不要执行
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            # data = self.data.get_request_data(i)  # 获取请求数据的关键字，还要根据这个倒接送里面拿数据
            data = self.data.get_data_for_json(i)
            header = self.data.is_header(i)  # 到这里我们主要的数据是不是就已经有了。
            if is_run:
                # method, url, data=None, header=None
                res = self.run_method.run_main(method, url, data, header)
                return res


if __name__ == "__main__":
    run = RunTest()
    print run.go_on_run()
