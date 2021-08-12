#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 8:41
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q653_findTarget.py
# @Note    :

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nums = []

        def mid_order(root):
            if root:
                mid_order(root.left)
                nums.append(root.val)
                mid_order(root.right)

        mid_order(root)
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == k:
                return True
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
        return False
