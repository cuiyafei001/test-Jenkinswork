#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : login.py
# @Author: Feng
# @Date  : 2018/12/27 14:19
# @Desc  :

from selenium import webdriver
import unittest
import time

# class Login(unittest.TestCase):
#
driver = webdriver.Firefox()
url = "http://10.111.2.162:8899/#/login"
driver.get(url)

driver.find_element_by_xpath(".//*[@type='text']").send_keys("cyf-01")
driver.find_element_by_xpath(".//*[@type='password']").send_keys("Abc123456.")

driver.find_element_by_xpath(".//*[@type='button']").click()


driver.quit()