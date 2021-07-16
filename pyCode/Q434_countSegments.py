#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/23 9:07
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q434_countSegments.py
# @Note    :

class Solution:
    def countSegments(self, s: str) -> int:

        s = s.split(" ")
        s = [i for i in s if len(i)>0]
        return len(s)