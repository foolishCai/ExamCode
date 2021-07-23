#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/23 8:51
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q605_canPlaceFlowers.py
# @Note    :


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count = count + 1
            if count >= n:
                return True
        return False

