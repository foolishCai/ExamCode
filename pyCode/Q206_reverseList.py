#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 8:56
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q206_reverseList.py
# @Note    :


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        return:
        type head: ListNode
		:rtype: ListNode
		"""
        # 申请两个节点，pre和 cur，pre指向None
        pre = None
        cur = head  # 遍历链表，while循环里面的内容其实可以写成一行 # 这里只做演示，就不搞那么骚气的写法了
        while cur: # 记录当前节点的下一个节点
            tmp = cur.next # 然后将当前节点指向pre
            cur.next = pre # pre和cur节点都前进一位
            pre = cur
            cur = tmp
        return pre