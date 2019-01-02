#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_ddt.py
# @Author: Feng
# @Date  : 2018/12/28 15:20
# @Desc  :

from Operation_project_automation.page.loginpage import LoginPage
from selenium import webdriver
import unittest
import ddt

# 参数和代码分离
testdata = [
            {"username": "cyf-01", "psw": "Abc123456.", "result": "cyf-01"},
            {"username": "cyf-02", "psw": "Abc123456", "result": ""},
            {"username": "cyf-03", "psw": "Abc1234",  "result": "Abc123456"},
            {"username": "cyf-04", "psw": "Abc12345",  "result": "cyf-"}]


@ddt.ddt
class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("开始测试")

    @ddt.data(*testdata)
    def test_login_01(self, canshu):
        print(canshu)
        print("账号：%s" % canshu["username"])
        print("密码：%s" % canshu["psw"])
        print("结果：%s" % canshu["result"])

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        print("结束")


if __name__ == "__main__":
    unittest.main()









