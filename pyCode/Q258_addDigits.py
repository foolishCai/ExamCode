#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 8:50
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q258_addDigits.py
# @Note    :

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            s = list(str(num))
            s = [int(i) for i in s]
            num = sum(s)
        return num
