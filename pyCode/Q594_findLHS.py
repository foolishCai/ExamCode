#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/20 8:39
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q594_findLHS.py
# @Note    :


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dicts={}
        for i in nums:
            dicts[i] = dicts.get(i, 0)+1
        res = 0
        for i in dicts:
            if i+1 in dicts:
                res = max(res, dicts[i]+dicts[i+1])
        return res
