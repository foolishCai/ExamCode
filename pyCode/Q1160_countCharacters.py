#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/15 8:55
# @Author  : Cai
# @File    : Q1160_countCharacters.py
# @Software: https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters/

import collections

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        cnt = collections.Counter(chars)
        for w in words:
            c = collections.Counter(w)
            if all([c[i] <= cnt[i] for i in c]):
                ans += len(w)
        return ans
