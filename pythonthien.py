# -*- coding: utf-8 -*-
"""2

Created on Sat Mar  6 10:52:12 2021

@author: DELL
"""
cot=int(input("so cot la :"))
hang=int(input("so hang la :"))
matrix = []
print("nhap so can nhap :")
for i in range(hang):
    a=[]
    for j in range(cot):
        a.append(int(input()))
    matrix.append(a)
for i in range (hang):
    for j in range(cot):
        print(matrix[i][j],end = "")
    print()
        