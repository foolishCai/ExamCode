#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/8 8:53
# @Author  : Cai
# @File    : Q705_MyHashSet.py
# @Software:

class MyHashSet:
    def __init__(self):
        self.mod = 1007
        self.table = [[] for _ in range(self.mod)]

    def hash(self, key):
        return key % self.mod

    def div(self, key):
        return key // self.mod

    def add(self, key):
        hash_key = self.hash(key)
        if not self.table[hash_key]:
            self.table[hash_key] = [0] * self.mod
        self.table[hash_key][self.div(key)] = 1

    def remove(self, key):
        hash_key = self.hash(key)
        if self.table[hash_key]:
            self.table[hash_key][self.div(key)] = 0

    def contains(self, key):
        hash_key = self.hash(key)
        return self.table[hash_key] != [] and self.table[hash_key][self.div(key)] == 1
