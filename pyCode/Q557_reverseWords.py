#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/6 8:39
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q557_reverseWords.py
# @Note    : https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split(" ")
        result = []
        for sl in sList:
            result.append(sl[::-1])
        return ' '.join(result)