#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 17:47
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q492_constructRectangle.py
# @Note    :

import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # 宽度从1开始
        w = 1
        # 长度L
        l = area // w
        # 遍历
        result = []
        # 从中间值开始向1值靠近，这样第一个满足area % w == 0的值就是所求列表
        w = int(math.sqrt(area))
        while w >= 1:
            if area % w == 0:
                return [area // w, w]
            w -= 1
        return result
