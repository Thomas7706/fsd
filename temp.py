#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:27:14 2024

@author: thomas
"""

#請撰寫一程式，讓使用者輸入攝氏溫度（度C），程式輸出華氏溫度（度F）。
#輸入＆輸出：
#輸入說明: 顯示提示文字 “請輸入攝氏溫度值: "
#輸出說明: 顯示“攝氏溫度為xx度，相當於華氏溫度為yy.yyy度”

tempC = eval (input("請輸入攝氏溫度值: "))   #tempC 是我們定義的攝氏溫度

tempF = tempC * (9/5) + 32
print("攝氏溫度",tempC,"度，相當於華氏溫度為",tempF,"度")
