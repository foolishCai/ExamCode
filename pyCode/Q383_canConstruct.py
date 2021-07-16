#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/24 9:16
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q383_canConstruct.py
# @Note    :

import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = collections.Counter(ransomNote)
        m = collections.Counter(magazine)
        if len(r.keys()) > len(m.keys()):
            return False
        tmp = [i for i in r.keys() if i not in m.keys() or r[i] > m[i]]
        if len(tmp) > 0:
            return False
        return True