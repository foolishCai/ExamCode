#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 11:11
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q556_matrixReshape.py
# @Note    :

import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        try:
            arr = np.array(mat).reshape(r, c)
            return arr.tolist()
        except:
            return mat