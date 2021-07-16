#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 8:52
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q530_getMinimumDifference.py
# @Note    :

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        pre,ans=float("-inf"), float("inf")
        stack=[]
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop(-1)
            ans=min(ans,abs(root.val-pre))
            pre=root.val
            root=root.right
        return ans
