#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 10:59
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q409_longestPalindrome.py
# @Note    : https://leetcode-cn.com/problems/longest-palindrome/solution/zui-chang-hui-wen-chuan-by-leetcode-solution/

import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        count = collections.Counter(s)
        for v in count.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
