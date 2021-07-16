#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 9:04
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q172_trailingZeroes.py
# @Note    :

class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = 0
        while n > 0:
            num += n // 5
            n = n // 5
        return num
