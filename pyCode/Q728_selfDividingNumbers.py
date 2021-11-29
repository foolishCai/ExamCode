#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/23 15:24
# @Author  : Cai
# @File    : Q728_selfDividingNumbers.py
# @Software:  https://leetcode-cn.com/problems/self-dividing-numbers/


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        r = []
        for i in range(left, right + 1):
            s = list(str(i))
            if "0" not in str(i):
                t = 1
                for z in s:
                    if i % int(z) != 0:
                        t = 0
                if t:
                    r.append(i)
        return r
