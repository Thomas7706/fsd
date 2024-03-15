#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 23:23:48 2024

@author: thomas
"""

#設計說明：撰寫一程式，讓使用者輸入一個數字n，則印出該數字的九九乘法表。
#範例：n = 6

n = int(input("請輸入數字："))

for i in range(1, 10):
    print("{} * {} = {}".format(n, i, n*i))