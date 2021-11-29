#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/17 11:12
# @Author  : Cai
# @File    : Q1624_maxLengthBetweenEqualCharacters.py
# @Software: https://leetcode-cn.com/problems/largest-substring-between-two-equal-characters/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n = len(s)
        ans = -1
        for i in range(n - 1):
            j = n - 1
            while j > 0:
                if s[j] == s[i]:
                    ans = max(ans, j - i - 1)
                    break
                j -= 1
        return ans