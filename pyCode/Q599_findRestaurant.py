#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/22 13:55
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q599_findRestaurant.py
# @Note    :


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        same = {i: list1.index(i) + list2.index(i) for i in list1 if i in list2}
        return [x for x in same if same[x] == min(same.values())]

