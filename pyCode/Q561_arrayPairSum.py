#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/8 9:14
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q561_arrayPairSum.py
# @Note    :

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])