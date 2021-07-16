#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 11:05
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q168_convertToTitle.py
# @Note    :

class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ''
        while n:
            n -= 1
            #ASCII码转大写字符 并且左加
            s = chr(65 + n % 26) + s
            n //= 26
        return s
