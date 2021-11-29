#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/25 15:24
# @Author  : Cai
# @File    : Q332_nextGreatestLetter.py
# @Software: https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        length = len(letters)
        left = 0
        right = length - 1
        while (left <= right):
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if left == length:
            return letters[0]
        else:
            return letters[left]