#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 10:15
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q506_findRelativeRanks.py
# @Note    : https://leetcode-cn.com/problems/relative-ranks/
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        hs = dict()
        for i, s in enumerate(score):
            hs[s] = i
        hs = sorted(hs.items(), key=lambda k: k[0], reverse=True)
        i = 1
        res = [0 for _ in range(len(score))]
        for k in hs:
            if i == 1:
                res[k[1]] = "Gold Medal"
            elif i == 2:
                res[k[1]] = "Silver Medal"
            elif i == 3:
                res[k[1]] = "Bronze Medal"
            else:
                res[k[1]] = str(i)
            i += 1
        return res

