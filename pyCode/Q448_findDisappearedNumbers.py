#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 9:33
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q448_findDisappearedNumbers.py
# @Note    :

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
                :type nums: List[int]
                :rtype: List[int]
                """
        for i, num in enumerate(nums):
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res