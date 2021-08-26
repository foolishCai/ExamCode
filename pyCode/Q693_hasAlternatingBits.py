#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-08-24
# @Author  : Cai
# @File    :
# @Software:

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        flag = n & 1
        n = n >> 1
        while n > 0:
            if flag == n & 1:
                return False
            flag = n & 1
            n = n >> 1
        return True

