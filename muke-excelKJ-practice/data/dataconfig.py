#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: mukeStudy_practice
#     FileName: dataconfig
#         Desc: 
#       Author: Administrator
#        Email: 136665323@qq.com
#     HomePage: dlmdlm.github.io
#       Create: 2018-10-11 10:33
#=============================================================================
"""
"""
excel常量：知道每一列放的是什么（获取每一行是什么，获取每一行的常量）


把这些他弄成变量的形式，然后去调用就可以了，这个是python的另一个知识点.class global_var:现在我们定义了一个类，这个类是变量
的形式，那现在我们就可以在类里面，把我们在表格里面需要的常量弄出来（请求方式，header，依赖数据，这些数据等等），我们把url，caseid，
，请求数据先默认写好，原因我们在说。首先caseId,然后等等，我们都搞定了。看下表格，表格里面暂时没有其他东西了，到现在为止，就我们就把常量
部分弄好了，那接下来，我们可以用一些方法，直接去获取数据，比如，我们要获取caseId,def get_id():如果觉得太麻烦了，没有关系，如果自己知道，可以写死
我们就是为了更活一点，这个时候，我们定义了一个方法，这个方法我们是可以直接调用的，因为这个方法在类里面，然后他返回的时候，return
可以直接去调用这个类，即 return global_var.Id,就可以这样调用。那现在我们可以把他所有的方法都可以弄进来。

7-7封装获取接口数据

好了，现在我知道每一列拿到的是什么，那我现在是不是要拿到每一行的数据，拿到数据后，还要去判断是否要执行，是post还是get，是否有header
拿到这些数据，然后结合我们的常量数据，做个判断然后再返回出去去执行。
那我们要怎么做呢，首先，我们在设计的时候，我们应该想，我们要有一个获取数据的地方，这些数据，就是我们excel里面每一行的数据，根据我们数据
的不同，然后返回不同的东西。建一个get_data.py文件。



"""


class global_var:
    # id
    Id = "0"

    request_name = "1"
    # url
    url = "2"
    # 是否运行
    run = "3"
    # 请求方式
    request_way = "4"
    # header
    header = "5"
    # 用例依赖
    case_depend = "6"
    # 数据依赖
    data_depengd = "7"
    #
    field_depengd = "8"
    # 请求数据
    data = "9"
    # 预期结果
    expect = "10"
    # 实际结果
    result = "11"


# 获取caseid
def get_id():
    return global_var.Id


def get_url():
    return global_var.url


# 获取运行方式
def get_run():
    return global_var.run


# 获取请求方式
def get_request_way():
    return global_var.request_way


# 获取请求头
def get_header():
    return global_var.header


# 获取数据依赖
def get_case_depend():
    return global_var.case_depend


def get_data_depend():
    return global_var.data_depengd


# 依赖数据所属字段
def get_field_depend():
    return global_var.field_depengd


# 获取请求数据
def get_data():
    return global_var.data


# 获取预期结果
def get_expect():
    return global_var.expect


# 获取实际结果
def get_result():
    return global_var.result


# 获取header的值,目前的话，先把header的值暂时写死，这个header的值是怎么来的，我们暂时不需要去搞明白，先放着。因为可能是写死的
# 也有可能是读取配置文件，也有可能是后面生成的。
def get_header_value():
    header = {
        "header": "1234",
        "cookie": "denglimei"
    }
