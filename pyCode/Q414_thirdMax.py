#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 9:21
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q414_thirdMax.py
# @Note    :

import collections
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        if len(c.keys())< 3:
            return max(c.keys())
        else:
            return sorted(c.keys())[::-1][2]
