#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/28 9:28
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q628_maximumProduct.py
# @Note    :

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[-1] * nums[-2] * nums[-3]
        b = nums[0] * nums[1] * nums[-1]
        return max(a, b)
