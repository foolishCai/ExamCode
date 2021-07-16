#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 8:53
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q205_isIsomorphic.py
# @Note    :

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sdict = {}
        tdict = {}
        for i in range(len(s)):
           if s[i] in sdict.keys() and t[i] in tdict.keys():
               if sdict[s[i]] != t[i] or tdict[t[i]] != s[i]:
                   return False
           elif s[i] not in sdict.keys() and t[i] not in tdict.keys():
               sdict[s[i]] = t[i]
               tdict[t[i]] = s[i]
           else:
               return False
        return True