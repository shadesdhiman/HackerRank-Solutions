# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 19:34:03 2021

@author: Dhiman
"""

def countingValleys(steps, path):
    # Write your code here
    depth = 0
    n = 0
    for i in range(len(path)):
       
        if(path[i] == 'U'):

            depth +=1
            
            
                   
        if(path[i] == 'D'):
            depth -=1
            if(depth == -1):
                n = n+1
            
               
    return n
x = "DDUUDDUDUUUD"
print(countingValleys(len(x),x))