# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 17:58:46 2021

@author: Dhiman
"""

def sockMerchant(n, ar):
    # Write your code here
    arr_dict = dict()
    summ = 0
    for i in range(len(ar)):
        if(ar[i] not in arr_dict):
            arr_dict[ar[i]] = 1
        else:
            arr_dict[ar[i]]+= 1
    
    for i in arr_dict:
        if arr_dict[i]%2 != 0:
            arr_dict[i]-=1
        else:
            x=1
        summ += arr_dict[i]

    return summ//2
print(sockMerchant(7,[10, 20, 20,20, 10, 10, 30, 50, 10, 20]))