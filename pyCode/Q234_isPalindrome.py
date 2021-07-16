#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/3 9:01
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q234_isPalindrome.py
# @Note    : https://leetcode-cn.com/problems/palindrome-linked-list/



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]