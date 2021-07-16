#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/15 10:36
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q757_distributeCandies.py
# @Note    :

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return int(min(len(set(candyType)), len(candyType)/2))