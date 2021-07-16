#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/25 8:39
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q338_countBits.py
# @Note    :

import collections

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            result.append(collections.Counter(bin(i))['1'])
        return result