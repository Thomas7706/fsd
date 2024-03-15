#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:09:12 2024

@author: thomas
"""

# BMI = 體重(kg)/身高(m2)
#輸入＆輸出：
#輸入說明: 分別顯示提示文字 “請輸入身高（cm）” 與 "請輸入體重(kg)"
#輸出說明：顯示“此人的BMI為：.....”
height = eval(input("請出入身高(cm): "))    #height 是我們定義的身高
weight = eval(input("請出入體重(kg): "))    #weight 是我們定義的身高 #eval 為定義為數值

BMI = weight/ ((height/100)**2)   # height/100 因為公分換算為公尺 ＃**2 為平方
print("此人的BMI為:", BMI)
