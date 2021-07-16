#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 8:40
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q217_containsDuplicate.py
# @Note    :

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return  True