#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: study-python
#     FileName: operationJson
#         Desc: 
#       Author: Administrator
#        Email: 136665323@qq.com
#     HomePage: dlmdlm.github.io
#       Create: 2018-09-04 17:49
#=============================================================================
"""
import json

"""
7-4学习操作json文件，
上节课我们已经学到了，如何操作excel，把excel重构封装了。现在呢，我们可以指拿打哪，目前看的话，我想获取拿到哪行的数据，
我就可以拿到。假如我们拿到excel数据,url
这节课，我们讲请求数据，一般的话，数请求据都是json格式，把请求数据弄成字典格式。如果请求数据的字段太多，全部写进那个
和excel文件里面，真的很影响美观，如何处理数据呢。eg：mushishi老师的方法，就是在表格里面，请求数据里面就写login一个字段，那
login字段我应该怎么去读他里面的数据呢。
然后login对应json数据重新建文件login.json，就是存储login的json数据，看到login就去取.json文件的数据.我只要告诉你
有login这个字段.JSON的格式类似这样{"username":"mushihsi","password":"111111"}。我们请求数据放到json文件里面，那意思就是
我要拿到login，就要拿到请求数据，既然说json是一个格式，那我们为是不是还可再外面给他包一层。就叫login
{"login":{"username":"mushihsi","password":"111111"}，
"loginout":{"username":"mushihsi","password":"111111"}，
"addcart":{"name":"denglimei"}
}那你现在要登录，那你就取login对应的请求数据，你要退出，你就取loginout对应的数据，那我们现在怎么根据关键字来取对应的请求数据呢
（那我们现在应该如何操作呢，按照请求数据的关键字，然后操作这个文件，然后把请求数据拿出来。那意思就是说，比如，我告诉你取login这个
的数据，你就把"login":{"username":"mushihsi","password":"111111"}这部分数据取出来）。写代码。一样的，在工具类包里main
创建一个operationJson.py文件。有了文件后，我们就需要import json 包。json包导入了之后呢，我还要干嘛呢。就需要去操作这个json，
同样的，我们定义一个类，

第一步打开：fp = open（"../dataconfig/login.json"）
第二步加载json文件：data = json.load(fp)
，弄出后，如果你要去操作数据，print data["login"]
接下来，我们应如何封装这个操作json的方法呢。

7-5讲解如何重构json工具类。

fp = open("D:/study-python/mukeStudy_practice/dataconfig/login.json")
data = json.load(fp) 
print data["login"]
首先我们还是定义一个类 class OperationJson，然后像操作excel一样。先去读取数据read_data（self），那他是怎么读取的呢，他首先
呢是open，open的是我们的json文件，这个时候我们发现，我们是把json文件拿出来了，拿出来了后，我们最后要关闭它，fp.close（），
否则他会一直在的,这样的化不太好，为了避免这种忘记close这种情况发生，然后python做了一个很人性化的，不会忘记。就是用了
另一个方法，用 
with open（../dataconfig/login.json）as fp
 data = json.load(fp)
 return data[],这样的话，我们是不是一样拿到了数据，把数据return出去，用完后，他就会自动关闭。
 好了，现在我们拿到了数据，那我们的下一步是什么呢。那我们的下一步想要得是，就是你调用我这个方法，只需要告诉我关键字，你告诉我
 关键字后，我就给你返回关键字带的，你想要的数据  -> def get_data(self):要把read_data这个拿下来，这种默认的时候？？
 是不是可以去构造函数里面解决，那变成了，def __init__(self):
                                        self.data = read_data.那数据是不是变成了这样。那好，def get_data哪里就变成了
   def get_data(self):
     self.data[id],给他传一个id，或者称之为key，传一个id进去就可以了。那我们把你的数据return掉， retunrn  self.data[id]
     最后执行的时候  if __name__=="__main__":
                    opjson = OperationJson()
                    opjson.get_data(),这样你传个关键字去，调用这个方法你就可以拿到关键字对应的这个数据了。
                                     
    7-6封装获取常量方法
    前面我们讲到了用过一个key拿到我们对应的json请求数据，那我们现在是拿到了json请求数据，然后我们思考 一下。
    当我们做一个接口测试自动化的时候，我们首先是不是要拿到他的测试用例表格的行数，然后拿到了行数后，要去拿他的 url
    ，拿请求方式，拿header，拿依赖数据，这些数据，我要一一拿出来，拿出来后，我们才能够依据一些逻辑判断，把它们组合在一起
    然后才能最后的执行case，假如是post的，那我们就去调用post的方法去执行，那我们接下里应该怎么做呢，我们现在是不是拿到了请求数据
    那我们是不是要把其他数据拿到，否则也是没有办法的，然后我们就想。我现在不是已经有了获取单元和单元格的内容吗？但是
    即使我们可以拿到了单元格的内容，我知道是拿哪个单元格吗？一个单元格是由行和列组成的，那么我假如拿到了其中一行，那拿列是不是要固定
    好，那我们是不是要有一个地方来存放这些常量，，存放一个常量，存放这些常量后，我们根据
    这个常量，来拿到这个单元格的列。列拿到了后，再通过我拿到的行数去循环每一行的时候，然后再根据行号，拿到行的数据，在进行数据拼接。
    所以接着，我们定义一个地方，就是存放我们常量的，所以我们来创建一个data包，这个data存放我们数据的包。这个包好了后，我们要
    创建这些数据，就是要存放的常量->创建一个dataconfig.py文件。然后在dataconfig这个文件里面，我们是不是要创建一个类。把这些他
    弄成变量的形式，然后去调用就可以了，这个是python的另一个知识点
                            


"""


class OperationJson:

    def __init__(self):
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open("F:/study-python/muke-excelKJ-practice/dataconfig/login.json") as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取数据
    def get_data(self, id):
        # print self.data[id]
        return self.data[id]


if __name__ == "__main__":
    opjson = OperationJson()
    print opjson.get_data("login")
