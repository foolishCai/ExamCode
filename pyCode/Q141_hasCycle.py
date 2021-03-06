#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 9:23
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q141_hasCycle.py
# @Note    :

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        return True
