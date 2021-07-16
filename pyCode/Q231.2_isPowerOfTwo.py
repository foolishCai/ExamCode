#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/1 9:04
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q231.2_isPowerOfTwo.py
# @Note    : https://leetcode-cn.com/problems/power-of-two/



class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1