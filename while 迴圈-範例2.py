#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:27:07 2024

@author: thomas
"""

#設計說明：撰寫一程式，讓程式產生0~9之間的一個密碼，然後讓使用者不段猜測，直到猜對為止。

import random

pwd = random.randint(0, 9)

guessNum = int(input("請輸入數字(0~9)："))

while guessNum != pwd:
    guessNum = int(input("猜錯，再猜(0~9)："))

print("猜對了，密碼就是", pwd)





