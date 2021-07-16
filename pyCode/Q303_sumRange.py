#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 9:04
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q303_sumRange.py
# @Note    : https://leetcode-cn.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        length = len(nums)
        self.sum = [0]*(length+1)
        for i in range(length):
            self.sum[i+1] = self.sum[i]+nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.sum[j+1]-self.sum[i]
