#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 9:12
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q171_titleToNumber.py
# @Note    :

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        sum = 0
        for i in range(len(columnTitle)):
            sum = sum * 26 + ord(columnTitle[i]) - 64
        return sum
