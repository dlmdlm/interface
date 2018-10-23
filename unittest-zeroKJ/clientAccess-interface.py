#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: first-test
#     FileName: clientAccess-interface
#         Desc: 
#       Author: Administrator
#        Email: 136665323@qq.com
#     HomePage: dlmdlm.github.io
#       Create: 2018-09-06 09:44
#=============================================================================
"""

import requests
import unittest
import HTMLTestRunner

# from demo import RunMain

"""
1.前面我们讲了去封装我们的接口测试的一个类，我们把几个方法都封装起来，只需要调用这个类就可以了，把需要的参数传给他，请求
方法等等，我们把一些请求方法给封装起来了，但是难道我们测试接口就是这样一步一步去测试吗？ 接下来，我们要讲到unittest这个
框架，是Python的一个框架我们要怎么去运用这个unittest呢，在python包里会自带这个unitest，如果你不确定是否有，老方法，
打开cmd，跑到python目录下然后执行import unittest  不会报错就是有的，不需要去安装他，一般默认是有这个包的。



2. 要怎么用呢，首先导入import unittest    #创建一个类的时候，必须要继承unittest，不可能是拿到unittest不做任何事情就可以
用他，所以必须要继class TestMethod(unittest.TestCase):  #相当于创建了测试类 ，然后测试类里面有很测试方法，不具体讲了，
但是unittest应该怎么用，以下是几个必须了解的方法
1.def setUp(self):   2.def tearDown(self):
    
 1.   #每次测试方法之前执行
    def setUp(self): #这个方法就是，在每个测试方法执行之前，都必须先去执行这个方法，是不能跳过这个方法的
        print "test-->setup"

 2.  #每次方法之后执行
    def tearDown(self):   #这个方法就是，在每个测试方法执行之后，都会去执行这个方法，是不能跳过这个方法的
        print "test-->teardown"

 3.   然后#创建一个方法，这个就是case，所有的case都要以test开头，否侧case没法执行
    def test_01(self):
        print"这是一个测试方法"

 4.  def test_02(self):
        print "这是第二个测试方法"
                                        5.   1.2.3.4.后，到目前为止，我们的类就写完了，然后下面我们写个入口来6. 
  6.if __name__=="__main__":  #入口，然后调用什么呢unittest.main(),
     unittest.main()

3.#有这种情况，就是执行一个测试方法的时候，不要每次都用setUp,因为我可能不用，比如说，一个登录，只需要登录一次就可以了，
不需要每次都登录#unittes里面有一个类方法，就是整个测试就只会执行一次，他需要一个注 解@，否则没有办法知道你这个是只执行
一次，还是每次都要执行#eg：get（cls）这个方法，我只需要一次，要注意的是，这个方法的名字不是你想怎么取就怎么取的，他是有
规定的那我们应该如何把unittest结合到我们刚刚封住好的脚本里面呢。
   @classmethod  
      def get(cls):  #这个是不执行的，名字不对
      print"这是只执行一次"             
   
    @classMethod
      def close（）   #这个也是不行的，名字不对
      
      #以下两个才是对的
    @classMethod 
    def setUpClass(cls):       #这个方法名是固定死的，不能没有@classMethod，必须按照类方法来， 否则会报错      
       print"只是类执行之前的方法"                                
       
    @classmethod
    def tearDownClass(cls): 
        print "类执行之后的方法"
前面讲了unittest，然后利用unittest去管理

"""


class TestMethod(unittest.TestCase):
    def setUp(self):

    # self.run = RunMain()

    def test_01(self):
        url = "http://m.imooc.com/passport/user/login"
        data = {
            "username": "131000000",
            "password": "hhhhhhhh",
            "verify": "",
            "referer": "https://m.imooc.com"
        }
        # run = RunMain()  #这样的话，我们用run去调用里面的方法就可以了，假如说
        res = self.run.run_main(url, "post", data)
        # self.assertEqual()
        print res
        # if res["errorCode"] ==1000:
        #     print "测试通过"
        # else：
        #     print"测试失败"
        # res = run.run_main(url,"post",data)

        # userid = 131000000000  #把他弄成一个全局变量globals，如下：
        globals()["userid"] = 1000909  # 这样就弄成一个全局变量了，这个时候在case就可以打印了

        @unittest.skip("test_02")

        print "这是我的第一个case"

    def test_02(self):
        # print userid
        url = "http://m.imooc.com/passport/user/login"
        data = {
            "username": "13100000000",
            "password": "hhhhhhh",
            "verify": "",
            "referer": "https://m.imooc.com"
        }
        res = self.run.run_main(url, "post", data)  # 这也有一个返回值赋值给res
        print res
        print "这是我的第二个case"


if __name__ == "__main__":
    # unittest.main()
    filepath = "../report/htmlreport.html"
    suite = unittest.TestSuite()
    suite.addTest(TestMethod("test_01"))
    suite.addTest(TestMethod("test_02"))
    unittest.TextTestRunner().run(suite)

"""
unittest和request重构封装
好了，到目前为止，我们的unittest方法只保留了两条case，但是现在有了case，但是我们要怎么做呢，我们刚刚写了一个demo.py这个
文件，这个demo是干什么的呢，就是我们运行接口测试的一个主方法，我只要传url，方法，data，然后调用这个方法方法就可以了，
那应该如何和unittest结合呢，
首先我们要思考的就是，这个demo要拿过来这里用，需要导进来（第18行），#from demo import RunMain  ，就会遇到一个问题，
当我们有很多包的时候，就是有很多文件，那他旁边就会有很多py文件，这样的话，就很不利于我们管理。那我就创建一个包，我们先
创建一个base文件夹，那我们怎么把base文件夹转换成包呢
python很简单，只要在这个文件下，创建一个_init_.py就可以了有了这个文件后，就是一个包了，那我们把这两个文件copy到里面。
那这样就有了 那这样的话，我base包里面管理文件，然后还可以创建其他的包管理文件，比如case，或者工具类的.

刚刚说到要把demo拿到haha.py文件中来，那拿进来之后要干嘛呢

我是不是可以把RunMain进行实例化一下 ：（ # run = RunMain()  #这样的话，我们用run去调用里面的方法就可以了，）
RunMain是个class所以要带括号 run=RunMain（），#这样的话，我们用run去调用里面的方法就可以了，假如说，我这个test_01要测，
测我们刚刚抓的一个接口，我们先把要的参数定义好，url，data，拿过来（第75,76行），那我们是不是直接可以用run.runmain,
把url，method，data传进去即 run.run_main(url,"post",data）,第83行。传进去了，那我们是不是执行完了，执行完了，
有个结果，把他赋给res，res = run.run_main(url,"post",data），现在我们打印一下res，print res
代码如下：【
url = "http://m.imooc.com/passport/user/login"
    data = {
        "username": "1310000000",
        "password": "hhhhhhh",
        "verify": "",
        "referer": "https://m.imooc.com"
    }
run = RunMain()
res = run.run_main(url,"post",data）
print res】

到了这里之后，我们又有了另外一个case，另一个case，数据可能不太一样，或者说，数据一样，我要执行两个case，那我们要怎么做呢。
同样的，这个case里面，在我们把url ，data copy过来，然后发现RunMain也要再次copy过去，觉得不太好啊，因为我刚刚已经实例化一次了，但是还实例化
一次，不太好吧，那怎么解决呢，我们刚刚是不是学了一个setUp,那我们是不是可以把run=RunMain（）放到setup里面，self.run=RunMain（）
当前类的整个,这样的话，每次运行case的都会去实例化，，视频里面学到，数据不能重复loads或者dumps。


                      unittest断言 ：assertEqual  

?????现在返回了那么多接口，那我怎么判断去运行接口，是失败与否，这么多case的情况应该怎么去判断呢
那我思考，我可不可以直接拿到返回结果去给他判断，如果你满足我的返回结果，
打印print type（res），打印看下是什么格式的。判断res是个字典（dict），那就可以用res去做判断了，我就说你是可以的,if res["errorode"] == 1000；
        if res["errorCode"] ==1000:
            print "测试通过"
        else：
            print"测试失败"
那我要每个case里面都要写上这么个判断，是不是觉得很麻烦,就要重复写很多了，那在我们的unittest里面有没有个官方断言呢，就是自己去判断
那肯定是有的，就不用自己判断了，self.assertEqual(self,first,second,msg=None)，assertEqual是验证， 你要干嘛，你要传两个参数，
他会验证first，second这
两个参数，一个默认的msg，那我们把第一个参数设置成“errorCode”，第二个设置成，1000那相等的话就没有下文了，那不相等的话，msg“测试失败”
assert有很多


                      unittest中case的管理及运用

                      global（）：全局变量;解决数据依赖

前面的课里我们讲到，在haha.py这个文件里面，我们把unittest，以及断言，把我之前封装的一个执行接口测试的方法引进来，然后封装在haha里面，现在
问题来了，我在执行case1和case2的时候，发现他们存在一个关系，case1的返回结果得一个值必须作为case2的一个接口请求参数，比如下单
case之间是相互独立的，这种情况应该怎么控制呢，接下来我们要讲的就是全局变量，和self不一样的全局变量
#把他弄成一个全局变量globals，如下： globals()["userid"] = 1000909 #这样就弄成一个全局变量了，这个时候在case就可以打印了
这样依赖问题就解决了，
注意：我们的unittest有个问题啊，就是他的执行顺序是根据字母顺序来排序执行的，先test_01,在02这样，如果有依赖关系的时候，一定要按照顺序来
尽量减少依赖执行，

                    跳过执行case
                    @unittest.skip()

现在我有有两个case，万一我有很多case，我只需要执行其中的一些，那我们怎么弄，这里就设涉及到unittest的一个容器
@unittest.skip(),括号里面要带着参数，是什么参数呢，就是我们case的名字.@unittest.skip("test_01"),我们在是不是可以打印下看下情况
在haha.py文件，我们用了@unittest.skip("test_02")，执行的时候就只会执行一个Test_01,因为test_02,已经跳过了。

到了这里，我们的整个流程差不多就就很清晰了，但是问题又来了，我们现在执行程序，都是通过unittest.main()这个方法的，执行的是
所有的unittest里面的testcase，那我们有没有其他的方式去执行，和main区别又是什么呢，
  
                  创建一个容器，unittest.TestSuite()
                  
首先，他算是创建了一个容器，就是我们放case的地方集合，首先就是创建一个容器，unittest.TestSuite(),创建之后呢就是命名
suite = unittest.TestSuite()。这个就是容器，然后就是往容器里面添加case，那应该怎么添加呢，suite.addTest(),是不是得知道类的名字

suite.addTest(testMethod（"test_02"）),需要几个case就添加几个。觉得已经全部添加好了，那我们就是可以去执行了。
则：unittest.TextTestRunner().run(),把我们的容器放进执行unittest.TextTestRunner().run(suite)
那到底有什么区别呢，一个是有容器的，一个是直接执行，现在我们看到都是，有容器的也是全部执行，没有的也是全部执行，那我有容器的
我就添加一个case进去，那他就会执行其中一个，

思考：如果我们的case放在N个py文件里面，那到底用那一种方式把不同py文件的case添加进来呢。在first-interface学习虫师的得到了解决

                 unittest和HTMLTestRunner结合生成报告

前面的课程我们将了unittest去管理case，然后怎么跳过case，等等。我们虽然把case都执行完了，但是我们不可能都按照这样去执行，
或者每次都去看他的控制台，那我们肯定要一个结果输出页面，那我们要怎么去把他的结果以页面的形式输出来呢。
测试报告该如何弄出来呢，Python里面有个开源的框架，叫HTMLTestRunner，百度-下载：然后复制粘贴到目录下的一个文件夹里面
然后要把这个文件复制到自己的python安装目录下下面的lib下面。copy进去就可以，如果不知道有没有copy成功，老方法，打开cmd
如果没有报错就是对的，OK了、
然后导入成功。导入成功后，在case里面我们应该怎么用他呢，同样，我们需要import,导入之后，我们应该怎么做呢，
我们只需要在最下面，在if __name__=="__main__":的最下面动点手脚，以上的代码，我们是用unittest.TextRunner去执行，
但是如果用HTMLTestRunner
不能这样，首先，我们要干一件什么事呢，就是我们的报告要生成在哪里？现在已经有HTMLTestRunner，但是要有一个地方写啊，报告生成在哪里
那我们是不是要定义一个文件路径，这个文件就是放我们报告的，filepath = "../report/htmlrpot.html",然后在文件下面创建一个htmlreport.html文件
那我现在有了文件，那我肯定还要一个资源流，fp = file（filepath，"wb"）,有了资源流，那我们就要把我们的unittest和HTMLTestRunner
结合起来，首先，我们要知道，我们要有个生成报告的，就是如何去运用HTMLTestRunner，
HTMLTestRunner.HTMLTestRunner() 里面需要有参数 有流，或者定义一下title  HTMLTestRunner.HTMLTestRunner(stream=fp,title="this isfirst report" )
接下类和unittest结合起来，赋值成一个变量 runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="this isfirst report" )
赋值成一个变量后，那我们是不是把我们的unittest拿进去了，运行它，runner.run（），把我们的主键拿进去runner.run（suite）

    #filepath = "../report/htmlreport.html"
    #fp = file(filepath,"wb")
    #suite = unittest.TestSuite()
    #suite.addTest(TestMethod("test_1"))
    #suite.addTest(TestMethod("test_2"))
    #runner = HTMLTestRunner.HTMLTestRunner(stram=fp,title="this isfirst report")
    #runner.run(suite)
    # unittest.TextTestRunner().run(suite)
    
    
    
    
    def test_02(self):
        url = "http://m.imooc.com/passport/user/login"
        data = {
            "username": "13100000",
            "password": "lllll",
            "verify": "",
            "referer": "https://m.imooc.com"
        }
        res = self.run.run_main(url, "post", data)
        self.assertEqual(res["status"], 10001,u"测试失败")
        print "这是第二个case"
        
        
        如何在接口开发阶段编写接口测试脚本
        前面的课程我们已经讲了unittest和request，仅仅是一些简单的使用。接下来说一个的概念，之前讲了前后端解耦
        不轮是前端开发，还是后端开发，我们都需要一个解耦，为什么呢，只有这样，才能并行工作，提高工作效率。
        测试也是一样的，不可能等接口开发完成，我们才开始开发测试框架，或者开始写测试用例，这样很会影响工作效率的
        那这个问题，我们应该如何来解决呢。先打开我们之前的一个工具fiddler，里面有个AUtoResponder，他有个自动回复的
        功能，
        ????我们在运行我写的脚本（first—test-base）的那两个接口，然后在fiddle哪里就可以看到两个请求。在inspectors-webforms可以看到发送请求的
        参数，在下面json哪里可以看到响应数据，
        (通过fiddler来模拟数据返回，实现在接口没有返回数据的情况下也可以进行编码，)
        接下来，我们来说mock，mock是用代码实现模拟返回数据，mock是怎么来的呢，打开cmd -->pip install mock 
        检查是否安装，输入python，  import mock
        
        
        安装好了，我们可以干嘛呢。怎么去运用他呢，现在我们来看看实现逻辑
        我们是在测试接口的时候，有url，有数据，然后调用self.runmain这个方法，再把url，data，方法传进去，
        我们的post，runmain的时候调用的是demo里面，runmain会根据你的方式method去选择是post还是get，跳转到post
        方法，执行完post方法的时候，会把结果返回出去，（   
        def send_post(self, url, data):
        res = requests.post(url=url, data=data).json()
        return res  res把结果返回出来了）
        即就是，在demo里面，res出来的就是一个结果。 res = self.run.run_main(url, "post", data)这就是一个结果
        那如果我们的接口没有开发完成，即使给了你数据，方法，data，也没有办法给我返回数据。那mock的作用就是
        就像fiddler一样，只是需要模拟返回数据，即我把url，data，method传给你，返给模拟数据，你就可以去断言了。
        （以上mock的实现原理）
        mock的代码实现。我们已经知道了mock的实现原理，那我们知道了现在要做的事就是把他的结果模拟返回出来，因为我们现在是没有接口的
        ，那我们只能通过模拟返回数据，那我们怎么用mock模拟返回数据呢。
        首先，我们需要把mock导进来，
        导入了之后呢，我们需要进行运用，
        我们在test01用例里面，mock.Mock
        有个方法提示，"return_value":the value returned when the mock is called .by default,意思就是调用mock的
        时候，会返回值，那返回的值是怎么样的呢，给return_value赋值return_value = data，把请求值赋给他，现在就是把data
        作为他的返回值，mock_data = mock.Mock(return_value = data),现在mock_data 就是一个值或者说是一个模拟的返回值。
        现在我们应该想的是，mock是然后一个方法，那我们可不可以直接把值赋给他，然后
        打印出来，我们先把mock_data打印出来，看下是什么样的。我们可以看到，告诉我们Mock id 是多少，
        那如果我们要用到这个mock，那是不是，我们刚刚说到的请求返回值 self.run.run_main(url, "post", data)返回出来的值要等于这个
        mock_data,
        self.run.run_main = mock_data,那现在我们是不是把你模拟请求的值给返回出来了。那我们是不是要去执行mock_data
        
        重构封装mock服务
        刚刚我们已经把mock在我们的方法里面实现了，但是看起来low，我们写一个case就要写个mock，就很重复啰嗦，那我们可不可以把他
        重构一下，封装一下。
        那如何封装呢，首先我们重新给他创建一个类，叫mock_demo.py,,创建好后，把mock导进来。
        思考:在刚刚的我们使用mock的过程中，mock充当的角色就是模拟结果返回的作用，那如果要封装起来，首先，给他弄成一个方法
        def mock_test():，在demo.py里面，run_main 方法有url，method，data，那我mock_test()里面是不是也要告诉我这些数据，
        那这些有了，那我们mock的时候，也要告诉是mock哪个方法，self.run.run_main,即要告诉我是mock哪个方法返回数据。
        所以模拟的方法也要封装进去，那也就变成了，首先，我要mock一个方法，然后把它的请求数据和响应数据给他返回出去，
        所以，把mock的这个语句拿进来mock_data = mock.Mock(return_value=data)【一个返回数据】
        
       那我们按照这个结构def mock_test(mock_method, request_data, url, method, response_data)把需要的东西都拿进来了，
       下面需要做什么呢，mock_method = mock.Mock(return_value=response_data)这样后，我们已经有了mock这个服务了，按照数据
       也已经返回会回来了，有一个mock，那我们是不是要像self.run.run_main = mock.Mock(return_value=data)这样一样，给他赋值，赋值后呢
       然后把它作为一个响应数给他返回出去 res = self.run.run_main(url, "post", data)
        
"""
