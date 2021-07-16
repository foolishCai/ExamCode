#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/16 8:54
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q589_preorder.py
# @Note    :


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(root: 'Node'):
            value.append(root.val)
            for child in root.children:
                dfs(child)

        value = []
        if root:
            dfs(root)
        return value
