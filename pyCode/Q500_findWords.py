#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 17:13
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q500_findWords.py
# @Note    :


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return list(filter(lambda word: any(set(word.lower()).issubset(line) for line in [set('asdfghjkl'),set('qwertyuiop'),set('zxcvbnm')]), words))
