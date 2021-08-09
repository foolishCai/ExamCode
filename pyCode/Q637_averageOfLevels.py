#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/2 9:04
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q637_averageOfLevels.py
# @Note    :


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        if root is None: return res
        que = [root]
        while que:
            n = len(que)
            Sum = 0
            for _ in range(n):
                cur = que.pop(0)
                Sum += cur.val
                if cur.left: que.append(cur.left)
                if cur.right: que.append(cur.right)
            res.append(Sum / n)
        return res
