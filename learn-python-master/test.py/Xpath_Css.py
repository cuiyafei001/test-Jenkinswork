#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Xpath_Css.py
# @Author: Feng
# @Date  : 2018/12/27 16:26
# @Desc  :


# xpath定位
"""
1、 .//*[@id="blog_nav_myhome"]  id定位
2、 .//*[@name='wd']             name定位
3、 .//*[@class='mnav']          class定位
4、 .//*[text()="文章"]          text定位
5、 .//*[@type="text"]           type值定位
6、 .//*[@id='blog_nav_newpost' and @class='menu']  id and class组合定位
7、 .//a[contains(text(),'管')]  text模糊匹配定位
8、 .//input[@id='su']           标签id定位
9、 .//*[@id='nr']/option[1]     id定位通过索引找到目标
10、.//*[@id='blog_nav_newpost']/../../.. 通过id找到他爷爷元素
11、.//*[@id='u_sp']/a[3]        定位父级元素id，通过索引找到子元素
"""

# css定位
"""
1、#blog_nav_newpost             id定位
2、.menu                         class定位
3、.lavalamp-item>a              上级标签定位到class
4、[type='text/css']             type定位
5、input                         标签定位
6、[name='word']                 name定位
"""