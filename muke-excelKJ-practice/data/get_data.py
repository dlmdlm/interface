#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: mukeStudy_practice
#     FileName: get_data
#         Desc: 
#       Author: Administrator
#        Email: 136665323@qq.com
#     HomePage: dlmdlm.github.io
#       Create: 2018-10-11 14:51
#=============================================================================
"""
"""
这个文件就是获取excel里每一行的数据文件(既获取一条case的数据)，获取数据

他有哪些东西呢，第一步，我们把需要的东西理一理，我们现在首先要干嘛，
首先，我们需要操作
excel，那我们是不是要把操作excel的这个包导入进来，from oprationExcel import OperationExcel,那现在我们要操作的数据已经有了，
那我们是不是还要把dataconfig.py这个文件拿进来,from dataconfig import *,现在我已经有了这两个东西，自觉得这个数据已经有了，
那现在是不是要创建一个一个类了，这个类我们要干嘛，就是去拿数据的，首先来说，我们在做测试的时候，要知道有多少行，所以我们要干的
就是要通过这个sheet，然后拿到这个的行数，这个时候我们想，在oprationExcel.py这个文件也是有可以获取行数的方法，那有什么不同吗？
没有什么不同的，就是拿的行数，就是为了方便统一，因为目前这个文件就是获取数据的一个文件，所以行数再拿一下。
方法名为 def get_case_lines(self):现在还需要有个东西，就是那个构造函数，因为我们需要把oprationExcel这个类拿进来，拿进来之后呢
需要把oprationExcel把他弄进去。弄进去之后，我们才能去操作我们的opraionExcel,才能拿到oprationExcel里面的数据，
那我们现在要干的一件事就是：去获取excel行数，就是我们的case个数  return self.opera_excel.get_lines()，到这里
我们就拿到这个行数了，那拿到了，我们就要看，你这行要不要执行，如果你要执行，我就给你返回true，不执行，我就给你返回fasle
那我们怎么封装好呢，def get_is_run(self):这个时候就需要另一个东西了，我要判断你是否执行，要get_cell_value()，传一个行号
和列号进去.那我要看这行是不是要执行，是不是要获取这行的
这个数据，那行我们是不是可以循环，那列我们是不是调用config，那我们是不是拿到行和列了。col = global_var.get_run()拿到了列
那我们是不是还要拿行，传进去def get_is_run(self, row):这样是否执行的数据就拿到了。赋给run_model,那拿到了后，进行判断
 if run_model == "yes":
            return True
        else:
            return False 这个时候看着代码有点low了，然后改成 加个flag。到现在，我们判断他是否执行是不是已经封装完了。判断他
是否执行之后，我们还要干嘛呢。还要看是否需要header,同样需要传行号和列号进去的.
       if header == "yes":
            return header,
        else:
            return None 这句话的意思：如果你有header，我就把header返回给你，因为我不知道你是不是要这个header的
            也不知道你这个header是什么样的，那我们是不是要有个地方去读取header，这个地方的header从哪里来呢
            现在可以说是放在这里的一个东西，也可能说要去读配置文件，或者我们要去操作我们的dataconfig.py这个文件，
# 获取header的值。到了这里，我们是否要携带header已经搞定了。然后现在我们是不是要判断，他是post还是get，
把各种数据封装取得，最后获取请求数据，我们要思考一下，就是有可能出现，url可能没有带请求参数，所以就需要判断一下
到目前为止，我们的数据是不是都获取完了呢。我们思考下，我们的请求数据拿到的是excel里面，那拿到了excel里面的数据，要不要去json
文件里面拿数据呢？我们应该怎么拿呢，那在上面我们是不是还要把json文件导进来啊。导进来之后我们才能去操作json

我们的数据处除了依赖部分就全部完成了，那剩下的事情就是把这些数据组装一下运行。
7-8post,get基类的封装
前面的课程我们已经讲到如何拿到excel的数据，我们已经把对excel的一些操作进行了封装，然后如何拿到数据，我们也已经弄了。正常的进程
我们是不是可以拿到数据去做接口测试，那本堂可课，我们就做一些最基础的封装，要封装那些东西呢，
首先，我们创一个runmethod.py文件。
"""
from util.operationJson import OperationJson
import dataconfig
from util.oprationExcel import OperationExcel


class GetData:

    def __init__(self):
        self.opera_excel = OperationExcel()

    # 去获取excel行数，就是我们的case个数
    def get_case_lines(self):
        # 把数据返回出去，那我们现在是不是拿到这个行数
        return self.opera_excel.get_lines()

    # 获取是否执行
    def get_is_run(self, row):
        flag = None
        # 行是传进去
        # 拿到了列
        col = int(dataconfig.get_run())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == "yes":
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def is_header(self, row):
        # 行是传进去
        # 拿到了列
        col = int(dataconfig.get_header())
        header = self.opera_excel.get_cell_value(row, col)
        if header == "yes":
            # return header,我不知道你这个header是什么样的，我们是不是要有个地方去去取header这个值
            return dataconfig.get_header_value()  # 拿到了这个header的值,在dataconfig里面写死的
        else:
            return None

    # 获取请求方式
    def get_request_method(self, row):
        col = int(dataconfig.get_request_way())
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    # 获取url
    def get_url(self, row):  # 行是传进去的
        col = int(dataconfig.get_url())  # 去dataconfig中取
        url = self.opera_excel.get_cell_value(row, col)
        return url

    # 获取请求数据
    def get_request_data(self, row):  # 行是传进去的
        col = int(dataconfig.get_data())  # 去dataconfig中取
        data = self.opera_excel.get_cell_value(row, col)  # 这个时候是不知道你的data有没有数据的,所以需要去判断一下
        if data == " ":
            return None
        else:
            return data

    # 通过获取关键字去json文件中去拿到数据，这个时候要把json文件导入进来
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data(row))  # 这里面需要的关键字是通过请求数据来的
        return request_data

        # 获取预期结果

    def get_expect_data(self, row):
        col = int(dataconfig.get_expect())
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == " ":
            return None
        else:
            return expect
