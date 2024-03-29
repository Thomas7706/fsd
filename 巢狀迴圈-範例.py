#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 19:50:48 2024

@author: thomas
"""

#範例1:兩位數的八進位數字
#撰寫一程式，列印兩位數的八進位數字，並且每一行列印八組數字，中間一個空白做間隔。
for i in range(8):
    for j in range(8):
        print(i, j, sep = "", end = " ")          #sep 指的是i跟j之間的間隔大小，預設為一個空格。
    print()        #外部的 print() 語句的作用是在內部的 for 迴圈執行完畢後，在每行的結尾打印一個空行。
                   #這是因為在 Python 中，print() 函式默認在輸出後會自動換行，也就是說，
                   #每次執行 print() 後，下一次執行 print() 打印的內容會自動移到下一行。
                   #因此，在每次內部的 for 迴圈執行完畢後，執行一次外部的 print() 就會換到下一行，
                   #從而形成了網格的行結構。

#------------------------------------------------------------------------------


#範例2:列印數字三角形
#撰寫一程式，第一排列印1~9，中間間一空白，第二排列印1~8，第三排1~7，以此類推。

for row in range(1,10):
    for col in range(1,10-row+1):
        print(col, end=" ")
    print()


#------------------------------------------------------------------------------


#範例3:列印九九乘法表。
#撰寫一程式，列印九九乘法表，並排列整齊。

for c in range(1,10):
    for d in range(2,10):
        print("{}*{}={:<2}".format(d,c,c*d), end=" ")  #{:<2} 代表留兩個位元的位子，並靠左對齊。
    print()

# {:<2} 是一個格式化字串中的部分，它指定了一個左對齊的填充方式以及最小寬度為 2 個字符。

# 這裡的含義是：

# <：表示左對齊，即數字在給定的寬度內左對齊填充。
# 2：表示最小寬度為 2 個字符。如果格式化後的字串長度小於 2，則會在右側填充空格以滿足最小寬度。
# 舉個例子，如果 c*d 的值為 6，則格式化後的結果為 "6 "，因為它佔用了兩個字符的寬度，左對齊填充，
# 並在右側填充一個空格以滿足最小寬度的要求。