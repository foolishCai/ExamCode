#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/11 9:16
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q268_missingNumber.py
# @Note    :

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = [i for i in range(n+1)]
        v = [i for i in s if i not in nums]
        return v[0]