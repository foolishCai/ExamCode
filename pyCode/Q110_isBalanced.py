#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 14:52
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q110_isBalanced.py
# @Note    :

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)