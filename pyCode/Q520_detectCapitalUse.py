#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 8:55
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q520_detectCapitalUse.py
# @Note    :

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word:
            return True
        elif word.lower() == word:
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        else:
            return False