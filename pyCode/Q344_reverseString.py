#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/17 8:52
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q344_reverseString.py
# @Note    :

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        return s