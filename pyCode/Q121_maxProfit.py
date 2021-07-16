#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 8:56
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q121_maxProfit.py
# @Note    :

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit
