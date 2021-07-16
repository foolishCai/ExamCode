#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 16:32
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q145_postorderTraversal.py
# @Note    :

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                res.append(root.val)
                root = root.right
            else:
                root = stack.pop()
                root = root.left
        return res[::-1]
