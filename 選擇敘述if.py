#!/usr/bin/env python3
# -*- coding: utf-8 -*-

score = int(input("你的成績是多少:"))

if score >= 95:
    print("帶你去歐洲玩")

else:
    print("哪兒都不去")


score = int(input("你的成績是多少:"))

if score>= 95:
    print("帶你去歐洲玩")

elif score>= 85:
    print("帶你去日本玩")

elif score>= 70:
    print("帶你去台灣玩")

else:
    print("哪兒都不去")
    
    
    
    
#巢狀判斷

sex = input("請問你的性別是(M/F): ")
height = eval(input("請問你的身高是 (cm): "))
weight = eval(input("請問你的身高是 (kg): "))

BMI = weight/ ((height/100)**2)   # height/100 因為公分換算為公尺 ＃**2 為平方

if sex == "M":    #如果是男生的情況下
    if BMI>25:
        print("體重過重")
    elif BMI<20:
        print("體重過輕")
    else:
        print("身材適中")
        
        
if sex == "F":
    if BMI>22:
        print("體重過重")
    elif BMI<18:
        print("體重過輕")
    else:
        print("身材適中")

else:
    print("輸入錯誤，無法判斷BMI")
            