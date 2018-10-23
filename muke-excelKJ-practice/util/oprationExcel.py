#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: study-python
#     FileName: oprationExcel
#         Desc: 
#       Author: Administrator
#        Email: 136665323@qq.com
#     HomePage: dlmdlm.github.io
#       Create: 2018-09-04 14:25
#=============================================================================
"""
import xlrd

# xlsfile = r"D:\study-python\dataconfig\interface.xls"
# book = xlrd.open_workbook(xlsfile)

"""
7-1如何设置一个接口自动化测试框架

如果我们要设置一个框架模型，我们要考虑那几点呢，接口地址，请求数据，接口类型（get、post），预期结果，接口自动化模型的话
还需要header，接口验证了你有没有登录，或者说有没有cookie保持登录状态，如果没有把登录状态传给他，就没有办法请求你的接口，
或者说请求了也会跳到登录页面去，还有数据依赖（重点难点）

7-2学习python操作excel获得内容

"""
"""前面我们讲了，我们把我们我们的接口case放到Excel里面，那我们思考接下来的第一步:要执行这些case，那我们要先拿到这些数据
其他的乱七八糟的事情先不用管，那我们要拿到这些数据是不是要一个方法（类）去操作这些数据，只有拿到这些数据才能做接下来
的事情，没有基础不知如何操作，打开百度：python操作excel->先安装xlrd（pip instal xlrd），然后导入。之前我们创建了一个
工具类的包init，我们的目的是操作excel里面的数据，那我们就要创建一个操作工具类的一个类，OperationExcel.py.要用到第三方的
库，所以先要引进来：import xlrd

#打开excel，弄成一个data对象
data = xlrd.open_workbook("D:\study-python\dataconfig\interface.xls")#文件的路径 ，刚刚已经打开excel了，然后就可以获取里面的数据了，
tables = data.sheets()[0]  拿到了第一个sheets的内容。通过sheet拿到数据，
print tables.nrows #打印出tables的行数
print tables.cell_value(2,3)#打印出第二行，第三列的表格的内容


7-3重构操作excel函数，以上是比较low的代码，我们要重构把他变得高大上些，以上的代码总共就才6行，看上去非常简洁，但是问题了
来了，我现在要去操作我们的excel，要去执行我们的excel，那我们遇到的问题会有，第一：我们不能把我们的路径写死，我也不知道
我的excel里面到底有多少行，那我们想，我现在可以拿到excel数据，那我们应该怎么封装一下。

首先我们来定义一个class，这个class就是用来操作表格的，然后我们首先定义get获取数据，目的就是加载出excel的数据
我希望我实例化类的时候，我就要拿到我的sheet数据，用到构造函数。
python知识点：类进行实例化的时候，会去调用一个构造函数，构造函数就是def__init__,这样的话，就是我实例化的时候
把file_name和sheet_id传进来，然后 这两句
self.file_name = file_name
self.sheet_id = sheet_id  全局化一下，然后后面就可以用了。然后觉得还是有点欠缺，现在数据是有了，但是每次实例化
的时候都要传个file_name 和 sheet_id ，而且我们有时候的case是固定的，，，，所以给他默认值，none。你可以传也可不传
，你传的时候就用你的，没有的话，我们做个判断，if存在我们就用你的这个，如果不存在，我们就默认给他一个，给他做了一个
容错处理。
获取拿sheets的内容，拿到excel里面的数据，然后我们要获取单元格的行数
       def get_lines(self):
        tables = self.data
        return tables.nrows
获取单元格内容
    def get_cell_value(self, row, col):
    return self.data.cell_value(row, col)
"""


class OperationExcel(object):  # 定义一个class，这个class就是用来操作excel的
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = "F:\study-python\muke-excelKJ-practice\dataconfig\interface.xls"
            self.sheet_id = 0
        self.data = self.get_data()

    # 第一步，获取拿sheets的内容，拿到excel里面的数据，
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        # 因为sheet里面拿到的不一定是0，或者啥的，所以，给他一个sheet_id，他应该是传进来的，
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取单元格内容
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)


# 实例化？？
if __name__ == "__main__":
    opers = OperationExcel()
    print opers.get_lines()
    print opers.get_cell_value(0, 0)
