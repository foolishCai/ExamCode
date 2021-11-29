#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/16 11:32
# @Author  : Cai
# @File    : Q717_isOneBitCharacter.py
# @Software: https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # 遍历数组，遇0 索引+1, 遇1索引+2
        n = len(bits)
        i = 0
        while i < n - 2:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        # 跳出循环后，如果直接跳到导数第二个位置，则做如下判断：
        if i == n - 2 and bits[-2] == 1:
            return False
        else:
            return True