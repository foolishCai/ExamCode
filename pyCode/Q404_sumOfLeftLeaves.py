#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 9:00
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q404_sumOfLeftLeaves.py
# @Note    :

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return None
            # 判断是否为左子节点，是否同时又是叶子节点
            if node.left and not node.left.left and not node.left.right:
                self.res += node.left.val #统计结果
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.res
