#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 8:33
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q521_findLUSlength.py
# @Note    :

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))