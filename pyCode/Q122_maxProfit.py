#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 9:05
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q122_maxProfit.py
# @Note    :


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0: profit += tmp
        return profit
# 策略是所有上涨交易日都买卖（赚到所有利润），所有下降交易日都不买卖（永不亏钱）。这个解释是真的很棒，我怎么就没想到这一层呢