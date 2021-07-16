#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 19:59
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q242_isAnagram.py
# @Note    :

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l_l = list(s)
        l_l.sort()
        s_l = "".join(l_l)
        l_r = list(t)
        l_r.sort()
        s_r = "".join(l_r)
        return s_l == s_r