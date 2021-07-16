#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 9:27
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q453_minMoves.py
# @Note    :

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums) if len(nums) != 1 else 0