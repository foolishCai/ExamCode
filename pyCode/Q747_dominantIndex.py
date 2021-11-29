#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 9:28
# @Author  : Cai
# @File    : Q747_dominantIndex.py
# @Software: https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        max_index = nums.index(max_num)
        if all(max_num >= 2 * x for x in nums if x != max_num):
            return max_index
        return -1
