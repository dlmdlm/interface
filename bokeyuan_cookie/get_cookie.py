#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: bokeyuan_cookie
#     FileName: get_cookie
#         Desc: 
#       Author: Administrator
#        Email: 136665323@qq.com
#     HomePage: dlmdlm.github.io
#       Create: 2018-09-21 14:30
#=============================================================================
"""
import requests

#先打开登录页面，获取部分cookie
url= "https://passport.cnblogs.com/user/signin"
headers = {
        "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
     }
s = requests.session()
r = s.get(url, headers=headers, verify=False)
print s.cookies

c = requests.cookies.RequestsCookieJar()

c.set(".CNBlogsCookie","A270D76743A68D272339175830A0FEF6F881D853089D00F326AC79DC4AAE235F3E3E254831CBF33C03865557E9D3A4932D4631191FFF96CE8CEDEB88B574C9C4A96D99FE6F342B132346B2EE50851E98F5A11BB4")
c.set(".Cnblogs.AspNetCore.Cookies", "CfDJ8J0rgDI0eRtJkfTEZKR_e83L3w4MutCgWBOOwMgNNTUC9Qg-L-YkeyTbcTjJiWkXrjvBkagGDlYckYtqMJ2ZrFsOc1TxAi5nZOmzB-11IZmB5efJYl7cfaN8vcGnOY3XIGT6hcrSmvQqGbf_ciMVggMrT99qlMJk9ROGNcQJ2VwFnrFejw7sPWiVa6cMafVjAo3MNkZReVNGIOavnzLNBOzfEiy5mAaTldIVbxdLAVY_PEqPBmRybzRUQTw3X6aEA_q-w9jb3LlebV_MRUE6-CnFnEMombRXQJMYVxsh3IcC")
s.cookies.updata(c)
print s.cookies

#登录成功后保存编辑内容
