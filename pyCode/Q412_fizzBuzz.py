#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/15 8:58
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q412_fizzBuzz.py
# @Note    :

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        r = []
        for i in range(n):
            if (i+1)%3 == 0 and (i+1)%5 == 0:
                r.append("FizzBuzz")
            elif (i+1)%5 == 0:
                r.append("Buzz")
            elif (i+1)%3 == 0:
                r.append("Fizz")
            else:
                r.append(str(i+1))
        return r