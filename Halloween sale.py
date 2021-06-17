# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 10:56:34 2021

@author: Dhiman
"""

def howManyGames(p, d, m, s):
                 #20 3 6 80
    # Return the number of games you can buy
    count = 0
    if p>s:
        return 0
    else:
        while(p>= m):
            
            count += 1
            s = s-p
            p -=d
            #print("Inside loop",p,d,m,s,count)
        #print("Outside",p,d,m,s, count)
        count += s//m
    return count

print(howManyGames(20,3,6,81))