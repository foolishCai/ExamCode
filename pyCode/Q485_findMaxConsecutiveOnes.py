#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/27 17:46
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q485_findMaxConsecutiveOnes.py
# @Note    :

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = -1
        res = 0
        for i, num in enumerate(nums):
            if num == 0:
                index = i
            else:
                res = max(res, i - index)
        return res