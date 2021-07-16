#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/23 10:24
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q461_hammingDistance.py
# @Note    : https://leetcode-cn.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')