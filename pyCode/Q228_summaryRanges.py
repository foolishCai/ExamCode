#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/26 11:07
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q228_summaryRanges.py
# @Note    :

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = 0
        res = []
        while n < len(nums):
            if n+1 < len(nums) and nums[n]+1 == nums[n+1]:
                m = n
                while n+1 < len(nums) and nums[n]+1 == nums[n+1]:
                    n += 1
                res.append("{}->{}".format(nums[m],nums[n]))
            else:
                res.append(str(nums[n]))
            n +=1
        return res