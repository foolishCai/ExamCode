#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 9:01
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q888_fairCandySwap.py
# @Note    :

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sumA, sumB = sum(A), sum(B)
        delta = (sumA - sumB) // 2
        rec = set(A)
        ans = None
        for y in B:
            x = y + delta
            if x in rec:
                ans = [x, y]
                break
        return ans