#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/26 9:08
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q606_tree2str.py
# @Note    :


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: TreeNode) -> str:
        def preorder(root):
            if not root:
                return ''
            if not root.left and root.right:  # 左边为空右边不为空的时需要加一个空括号保证映射关系
                return str(root.val) + '()' + '(' + preorder(root.right) + ')'
            if root.left and not root.right:
                return str(root.val) + '(' + preorder(root.left) + ')'
            if not root.left and not root.right:
                return str(root.val)
            return str(root.val) + '(' + preorder(root.left) + ')' + '(' + preorder(root.right) + ')'

        return preorder(root)
