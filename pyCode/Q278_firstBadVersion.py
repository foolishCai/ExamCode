#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/12 9:35
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q278_firstBadVersion.py
# @Note    :

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = left + (right - left) / 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left