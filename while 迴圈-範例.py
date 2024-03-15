#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:45:04 2024

@author: thomas
"""

#設計說明：撰寫一程式，讓使用者輸入一個數字n，用while迴圈，用＠字元列印出n層的直角三角形。
#範例：n = 7

n = int(input("請輸入數字："))

i = 1
while i <= n:
    print("@"*i)
    i += 1

#------------------------------------------------------------------------------

import random    #語法 random.randint(a,b) 代表隨機取出a到b之間的整數，包含a和b。

for c in range(10):
    print( random.randint(1, 50) )
