#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/31 9:04
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q160_getIntersectionNode.py
# @Note    : https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        nodeA = headA
        nodeB = headB
        while (nodeA != nodeB):
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        return nodeA
