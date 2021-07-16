#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 8:38
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q551_checkRecord.py
# @Note    :

class Solution:
    def checkRecord(self, s: str) -> bool:
        def pending_s(s):
            count = 0
            for i in range(0, len(s)):
                if s[i] == "L":
                    count += 1
                    if count > 2:
                        return False
                else:
                    count = 0
            return True
        return s.count("A") <= 1 and pending_s(s)
