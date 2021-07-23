#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/19 9:58
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q590_postorder.py
# @Note    :

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> List[int]:
        def dfs(root: Node) -> None:
            for child in root.children:
                dfs(child)
            value.append(root.val)

        value = []
        if root:
            dfs(root)
        return value
