#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 16:35
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q476_findComplement.py
# @Note    :

class Solution:
    def findComplement(self, num: int) -> int:
        """
        :type num: int
        :rtype: int
        """
        index = bin(num)[2:].find('0')
        if index == -1:
            return 0
        return int('0b'+''.join(['1' if b == '0' else '0' for b in bin(num)[index:]]), 2)
