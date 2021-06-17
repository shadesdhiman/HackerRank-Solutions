# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:13:29 2021

@author: Dhiman
"""

def getMoneySpent(keyboards, drives, b):
    #
    keyboards.sort()
    drives.sort()
    maxi = 0
    print(keyboards,drives)
    maxi = keyboards[0]+drives[0]
    if(maxi>=b):
        return -1
    # Write your code here.
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            temp = keyboards[i]+drives[j]
            if(b>temp and maxi<temp):
                maxi = temp
    return maxi

b = 10
keyboards = [3]
drives = [5,10,7]
print(getMoneySpent(keyboards,drives,b))