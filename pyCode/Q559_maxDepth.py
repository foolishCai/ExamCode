#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/7 9:29
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q559_maxDepth.py
# @Note    :


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:
        if not root:
            return 0
        d = 1
        for child in root.children:
            d = max(d, self.maxDepth(child) + 1)
        return d
