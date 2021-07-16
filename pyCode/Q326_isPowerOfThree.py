#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/18 8:50
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q326_isPowerOfThree.py
# @Note    :

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        if (n == 0 or n % 3 != 0):
            return False
        return self.isPowerOfThree(n/3)
