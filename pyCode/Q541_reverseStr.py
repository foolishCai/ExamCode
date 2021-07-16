#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 9:41
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q541_reverseStr.py
# @Note    :

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result=''
        for i in range(0, len(s), 2*k):
            tmp = s[i:i+k]
            tmp = tmp[::-1]+s[i+k:i+2*k]
            result += tmp
        return result