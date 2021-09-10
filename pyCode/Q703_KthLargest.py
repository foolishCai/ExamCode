#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/6 15:22
# @Author  : Cai
# @File    : Q703_KthLargest.py
# @Note: https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []
        for x in nums:
            heapq.heappush(self.minHeap, x)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]
