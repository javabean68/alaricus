#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 08:42:25 2017

@author: Anna Salvi
"""

print(3)



var = input('Nummer: ')
print ("war", var)


operation=input('Operation: ')
print ("war",operation)

var2=input('Nummer: ')
print ("war", var2)


if operation=='x':
    ergebnis = int(var)* int(var2)
    print('Ergebnis war', ergebnis)  
elif operation=='+':
    ergebnis = int(var)+ int(var2)
    print('Ergebnis war', ergebnis)  

