# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:21:57 2021

@author: Quina
"""

a = input("Please enter a 4 character string")
b = ''
    
for i in a :
    if ord(i) >= 90:
        i = chr(ord(i)-32)
        b = b + i
        
print(b)
print("the string capitalizatin is",b)