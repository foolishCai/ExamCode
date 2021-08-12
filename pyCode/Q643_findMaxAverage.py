#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 9:37
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q643_findMaxAverage.py
# @Note    : https://leetcode-cn.com/problems/maximum-average-subarray-i/


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = 0
        largest = float('-inf')
        for i, num in enumerate(nums):
            sums += num
            if i >= k:
                sums -= nums[i - k]
            if i >= k - 1:
                largest = max(sums, largest)
        return largest / float(k)
