#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 10:35
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q504_convertToBase7.py
# @Note    : https://leetcode-cn.com/problems/base-7/

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0:
            return "-" + self.convertToBase7(-num)
        if num < 7:
            return str(num)
        return self.convertToBase7(num // 7) + str(num % 7)