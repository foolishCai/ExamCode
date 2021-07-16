#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 14:24
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q44_arrangeCoins.py
# @Note    :

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        flag = 0
        while n >= 0:
            flag = flag + 1
            n = n - flag

        return flag - 1