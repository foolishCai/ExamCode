#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/5 8:51
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q237_deleteNode.py
# @Note    :

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

