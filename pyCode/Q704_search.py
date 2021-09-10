#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/7 17:48
# @Author  : Cai
# @File    : Q704_search.py
# @Software:


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1