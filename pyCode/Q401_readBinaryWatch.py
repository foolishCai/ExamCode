#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 9:06
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q401_readBinaryWatch.py
# @Note    : https://leetcode-cn.com/problems/binary-watch/

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        hours = [1, 2, 4, 8, 0, 0, 0, 0, 0, 0]
        minutes = [0, 0, 0, 0, 1, 2, 4, 8, 16, 32]
        res = []

        def backtrack(num, index, hour, minute):
            if hour > 11 or minute > 59:
                return
            if num == 0:
                res.append('%d:%02d' % (hour, minute))
                return
            for i in range(index, 10):
                backtrack(num - 1, i + 1, hour + hours[i], minute + minutes[i])

        backtrack(num, 0, 0, 0)
        return res