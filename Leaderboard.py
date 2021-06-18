# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 00:10:50 2021

@author: Dhiman
"""
from bisect import bisect

def climbingLeaderboard(s,t):
    s.sort()
    k =len(t)
    y = len(s)
    for i in range(k):
    	print(y - bisect(s, t[i]) + 1)
        
print(climbingLeaderboard([100,90,90,80,75,60],[50,40,120,30,75,70,73,72,102,30,20]))

#100 90 80 77 75 65 60 50