#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 9:08
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q232_MyQueue.py
# @Note    :

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.stack1:
            self.front = x
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.front = None
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2:
            return self.stack2[-1]
        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack1 and not self.stack2