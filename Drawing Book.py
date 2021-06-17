# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:57:16 2021

@author: Dhiman
"""

def pageCount(n, p):
    turn_f = 0
    # Write your code here
    Last_page_both_side = None
    if (n%2 == 0):
        Last_page_both_side  =True
    else:
        Last_page_both_side = False
    if p == 1:
        return 0
    if p ==2:
        return 1
    
    turn_f = p//2
        
    if (Last_page_both_side == True):
        turn_b =  ((n-1-p)//2)+1
 
    else:
        turn_b = (n-p)//2
   
    return min(turn_f, turn_b)
               
            
        
        
print(pageCount(6,2))