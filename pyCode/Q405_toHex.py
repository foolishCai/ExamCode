#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 11:54
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q405_toHex.py
# @Note    :
class Solution:
    def toHex(self, num: int) -> str:
       return hex(num&0xFFFFFFFF)[2:]