# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 13:02:06 2021

@author: Dhiman
"""

import math
def workbook(n, k, arr):
    # Write your code here
    page = 0
    special = 0
    for i in range(n):
        page +=1
        pro_count = arr[i]
        for j in range(1,arr[i]+1):
            if (j == page):
                #print(j)
                special +=1
            
            #print(j, page, pro_count)
            if(pro_count>1):
                if(j%k==0):
                    page +=1
            
            pro_count-=1
            
                  
    return special
            
print(workbook(5,3, [4,2,6,1,10]))  