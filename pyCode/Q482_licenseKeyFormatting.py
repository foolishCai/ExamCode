#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 9:34
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q482_licenseKeyFormatting.py
# @Note    :

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        # 逆序思维，假如题目中第一组的条件是用在最后一组，是不是很容易做：遇到合适索引就拼接-
        # 所以本题将字符串翻转一下，然后每次换成前插就好了
        s = S.upper().replace('-','')[::-1]
        res = ''
        for i in range(len(s)):
            if i%K == 0 and i!=0: res = '-' + res
            res = s[i] + res
        return res