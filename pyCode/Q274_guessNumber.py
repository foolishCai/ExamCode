#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/23 9:00
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q274_guessNumber.py
# @Note    :

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = (l + r) >> 1
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                r = mid - 1
            elif guess(mid) == 1:
                l = mid + 1
