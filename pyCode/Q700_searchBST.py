#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/31 15:40
# @Author  : Cai
# @File    : Q700_searchBST.py
# @Software:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # 迭代
        while root:
            if root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
            else:
                return root
        return None
