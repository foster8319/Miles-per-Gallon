# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:29:45 2019

@author: fostere8319
"""
Miles= 0
Miles_Counter = 0


Gallons_Used = float(input("Enter Gallons Used between 0-26 or -1 to terminate program: "))

while Gallons_Used !=-1: 
    Miles += Miles
    Miles_Counter +=1 
    Miles_Driven = float(input("Enter Miles Driven between 0-700 or -1 to terminate program: "))
    
    Miles = Miles_Driven/Gallons_Used
    print("The Miles/Gallons for this tank was",Miles)
   
    
    
    Gallons_Used = float(input("Enter Gallons Used between 0-26 or -1 to terminate program: "))

if Miles_Counter !=0:
    Average = Miles/Miles_Counter
    print("Average:",Average)
