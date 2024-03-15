#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 19:56:51 2024

@author: thomas
"""
#練習2

year = eval(input("請輸入一個西元年年份："))

if year >= 0:
    if year % 400 == 0:
        print("{}年是閏年".format(year))
    
    elif year % 100 == 0:
        print("{}年不是閏年".format(year))
    
    elif year % 4 == 0:
        print("{}年是閏年".format(year))
        
    else:
        print("{}年不是閏年".format(year))

if year < 0:
    print("請輸入正確的年份")