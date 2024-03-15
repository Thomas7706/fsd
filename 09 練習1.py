#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:33:41 2024

@author: thomas
"""


#練習1-1, #練習1-2 combine


a = eval(input("請輸入第一個整數a: "))
b = eval(input("請輸入第二個整數b: "))
sign = input("請輸入運算子(+, -, %, //, *, /, **): ")  #sign 會輸入符號，所以不用加eval

if sign == "+":
    print("{}{}{} = {}".format(a,sign,b,a+b))



elif sign == "-":
    print("{}{}{} = {}".format(a,sign,b,a-b))



elif sign == "%":
    if b == 0:
        print("除數不可為零")
    else:
        print("{}{}{} = {}".format(a,sign,b,a%b))



elif sign == "//":
    if b == 0:
        print("除數不可為零")
    else:
        print("{}{}{} = {}".format(a,sign,b,a//b))
 


elif sign == "*":
    print("{}{}{} = {}".format(a,sign,b,a*b))
    
    
    
elif sign == "/":
    if b == 0:
        print("除數不可為零")
    else:
        print("{}{}{} = {}".format(a,sign,b,a/b))

    
    
elif sign == "//":
    print("{}{}{} = {}".format(a,sign,b,a**b))



else:
    print("輸入錯誤，無法運算")






