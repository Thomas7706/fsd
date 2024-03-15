#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 19:15:51 2024

@author: thomas
"""

#撰寫一程式，讓使用者輸入平面座標上，A點(x1,y1)與B點(x2,y2)的座標值，並輸出正確的座標顯示與兩點的距離。
#座標距離輸出到小數點後4位。
#輸入＆輸出：
#輸入說明: 分別顯示提示文字：“輸入A點的x座標”，“輸入A點的y座標”，“輸入B點的x座標”，“輸入B點的y座標”
#輸出說明: 顯示“A點的座標為(x1,y1)“，“B點的座標為(x2,y2)“，“兩點距離為x.xxxx”。

x1 = eval(input("輸入A點的x座標"))
y1 = eval(input("輸入A點的y座標"))
x2 = eval(input("輸入B點的x座標"))
y2 = eval(input("輸入B點的y座標"))

distance = ((x1-x2)**2 + (y1-y2)**2)**0.5

print("A點座標為", (x1,y1))
print("B點座標為", (x2,y2))
print("兩點的距離為{:.4f}".format(distance))