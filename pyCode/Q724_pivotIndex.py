#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/19 10:22
# @Author  : Cai
# @File    : Q724_pivotIndex.py
# @Software:

class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        pre_sum = 0
        for i in range(len(nums)):
            if total - nums[i] == pre_sum * 2:
                return i
            pre_sum += nums[i]
        return -1
