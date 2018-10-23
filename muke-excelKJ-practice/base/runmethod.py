#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: mukeStudy_practice
#     FileName: runmethod
#         Desc: 
#       Author: Administrator
#        Email: 136665323@qq.com
#     HomePage: dlmdlm.github.io
#       Create: 2018-10-11 17:17
#=============================================================================
"""
"""
最基础基础的封装，最基础的请求方式


首先，我们要导入request，然后创建一个类class RunMethod:，然后创建三个方法，一个是post，一个是get，一个是主函数
按照我们现在的逻辑，应该就是这样的，我主函数只要穿method, url, data, header。传进来就可以，   
 def post_main(self, url, data, header):
        pass
    
    def get_main(self, url, data, header):
        pass
    
    def run_main(self, method, url, data, header):
        pass
现在我们来完善这些方法，先前我们说过，url有没有可能为空，不可能，data可不可能为空，有可能，header有没有可能为空，有可能
method不可能为空。所以我们是不是要做个判断，首先就为none.这个时候是不是可以按照之前的那个，判断header是否为空，然后去执行
他的一个接口
        if header !=None
            requests.post(url=url, data=data, headers=header)
        else:
            requests.post(url=url, data=data)如果header不为空就发送带header的参数，如果为空，就发不带header的参数，这个是和
前面，我们讲demo的不同之处。然出后把我们的接口返回出去，首先，我们的接口一开始为None(res = None),如果有就结果就返回。。
如果接口出错或者程序出错，就没有了返。正常情况下，是不是就可以吧结果返回出去了，但是，一般情况下，我们需要把结果弄出来，
现在是没有结果的啊，我们测试的结果，一般是json的，所以json处理一下.现在的话，我们的结果就有了，他是以json格式为结果的。
这个时候，我们还是需要把结果好好处理一下的，因为有时候，他的结果是很不友善的，到后面看到了就知道了（现在暂时没有处理），
现在我们把run_main弄好，同样method不可能为空，data如果是get请求是可能为空的，header也可能为空，
然后我们就需要去判断了，判断你的method是post还是get
    if method =="post":
            self.post_main(url, data, header)  # 如果这里header传了空，然后调用post方法，正常是没事的，所以这里先不判断
        else:
            self.get_main(url, data, header)
这个时候，调用方法的时候，他是不是要给我们返回一个值啊，我们是不是把那个值记录下来，res=none,同样的。是不是需要把值返回出去
return res,到目前为止，这个方法，我们是不是就是完事了。现在就只是找个地方调用run_mian然后把数据传进去。
那这个就去主流程哪里控制了，
7-9主流程封装及错误解决调试。
前面我们已经讲了发送接口测试的方法，给他封装了起来，而且把他放在了一个类里面，通过我们的主函数去调用就可以，那这个时候我们主要
在我们的主流程里面一个方法里面根据我们的一些执行条件去调用他就可以了。那现在我们要怎么实现我们的主流程呢，我们思考一下
我们的主流程我们需要干那些事情呢，现在，我们已经有了excel，excel里面已经把我们的接口地址以及是否执行，请求数据什么的都有了，然后
json数据也几经弄好了，这节课我们来讲整个主流程的一个入口。
我们再创建一个文件夹，就是一个主要程序的一个入口。我们首先也是创建一个包的形式。然后再包里面创建一个run_test文件，


"""
import requests


class RunMethod:
    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header).json()
        else:
            res = requests.post(url=url, data=data).json()
        return res

    def get_main(self, url, data, header=None):  # 这里面有个坑，看后面可不可以填平
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header).json()
        else:
            res = requests.get(url=url, data=data).json()
        return res

    def run_main(self, method, url, data=None, header=None):
        res = None  # 调用这个方法的时候需要返回出去，记录在这里
        if method == "post":
            res = self.post_main(url, data, header)  # 如果这里header传了空，然后调用post方法，正常是没事的，所以这里先不判断
        else:
            res = self.get_main(url, data, header)
        return res
