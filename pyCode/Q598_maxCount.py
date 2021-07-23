#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 16:46
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q598_maxCount.py
# @Note    :

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return min([a[0] for a in ops]) * min([a[1] for a in ops]) if ops else m * n

