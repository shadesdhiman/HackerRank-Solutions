# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 13:15:38 2021

@author: Dhiman
"""


def maximumSum(a, m):
    # Write your code here
    maxi = 0

    for i in range(len(a)):
        summ =0
        for j in range(i,len(a)):
            summ += a[j]
            print(j,a[j],summ,maxi)
            if(maxi< summ%m):
                maxi = summ%m
                
    return maxi
    
print(maximumSum([1,1,1,1,1,1],7))