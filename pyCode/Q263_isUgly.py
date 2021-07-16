#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 8:46
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q263_isUgly.py
# @Note    :

class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 2:
            return False
        while n != 1:
            if n % 2 == 0:
                n /= 2
            elif n % 3 == 0:
                n /= 3
            elif n % 5 == 0:
                n /= 5
            else:
                return False
        return True