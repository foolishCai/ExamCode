#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/22 8:51
# @Author  : Cai
# @File    : Q762_countPrimeSetBits.py
# @Software:


class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        res = 0
        def helper(n):
            if n == 1: return False
            for i in range(2, int(n**0.5)+1):
                if n%i == 0:
                    return False
            return True
        for i in range(L, R+1):
            n = bin(i)[2:].count('1')
            if helper(n):
                res += 1
        return res
