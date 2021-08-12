#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 8:51
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q661_imageSmoother.py
# @Note    : https://leetcode-cn.com/problems/image-smoother/


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        ans = [[0] * len(M[0]) for _ in M]
        for row, col in [(i, j) for i in range(len(M)) for j in range(len(M[0]))]:
            count = 0
            for dx, dy in [(i, j) for i in range(row - 1,row + 2) for j in range(col - 1, col + 2)]:
                if 0 <= dx < len(M) and 0 <= dy < len(M[0]):
                    ans[row][col] += M[dx][dy]
                    count += 1
            ans[row][col] //= count
        return ans