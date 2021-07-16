#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 10:37
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q837_new21Game.py
# @Note    : https://leetcode-cn.com/problems/new-21-game/


class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1.0
        dp = [0.0] * (K + W + 1)
        for i in range(K, min(N, K + W - 1) + 1):
            dp[i] = 1.0
        dp[K - 1] = float(min(N - K + 1, W)) / W
        for i in range(K - 2, -1, -1):
            dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
        return dp[0]
