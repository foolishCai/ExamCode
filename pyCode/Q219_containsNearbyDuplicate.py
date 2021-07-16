#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/24 8:55
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q219_containsNearbyDuplicate.py
# @Note    : https://leetcode-cn.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for idx, n in enumerate(nums):
            if n not in hash_map or (idx - hash_map[n]) > k:  # 情况1 & 情况2
                hash_map[n] = idx
            else:  # 情况3
                return True
        return False
