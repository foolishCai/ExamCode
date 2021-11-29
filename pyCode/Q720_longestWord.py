#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/18 8:57
# @Author  : Cai
# @File    : Q720_longestWord.py
# @Software: https://leetcode-cn.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        maxword = ""
        se = set()
        for word in words:
            if len(word) == 1 or word[:-1] in se:
                se.add(word)
                if len(word) > len(maxword):
                    maxword = word
        return maxword
