#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 10:40
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q496_nextGreaterElement.py
# @Note    :


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = []
        d = {}
        ans = []
        for i in range(len(nums2)):
            while s  and nums2[s[-1]] < nums2[i]:
                d[nums2[s[-1]]] = nums2[i]
                s.pop()
            s.append(i)
        for i in nums1:
            ans.append(d.get(i,-1))
        return ans
