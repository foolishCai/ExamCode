#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/16 9:16
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q292_canWinNim.py
# @Note    : https://leetcode-cn.com/problems/nim-game/

class Solution:
    def canWinNim(self, n: int) -> bool:
        return (n % 4 != 0)
