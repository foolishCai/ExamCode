#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 8:39
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q645_findErrorNums.py
# @Note    : https://leetcode-cn.com/problems/set-mismatch/

import collections
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)

        a, b = 0, 0
        for num in range(1, len(nums) + 1):
            if c[num] == 0:
                b = num
            if c[num] == 2:
                a = num

        return [a, b]