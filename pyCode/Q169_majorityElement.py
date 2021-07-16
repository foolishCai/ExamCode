#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 10:28
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q169_majorityElement.py
# @Note    :
import collections
import numpy as np

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = np.floor(len(nums)/2)
        c = collections.Counter(nums)
        return [k for k,v in c.items() if v>n][0]
