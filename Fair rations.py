# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:17:57 2021

@author: Dhiman
"""

def fairRations(B):
    # Write your code here
    count = 0
    if(len(B)==2):
        if B[0]%2 == 0:
            if(B[1]%2==0):
                return  '0'
            else:
                return 'NO'
        else:
            if (B[1]%2!=0):
                return '2'
            else :
                return 'NO'
    else:
        for i in range(len(B)):
            print(B)
            if(i == 0 and B[i]%2!= 0 ):
                
                B[0]+=1
                B[1]+=1
                count+=2
            elif(i==0 and B[i]%2 ==0):
                #print("*")
                continue
            elif(B[i]%2!=0 and i != 0 ):
                print(B[i],i)
                B[i]+=1
                count = count+1
                if(i+1 < len(B)):
                    B[i+1]+=1
                    count+=1
                else:
                    return 'NO'
            else:
                continue
                    
    print(B)
    for i in range(len(B)):
        if (B[i]%2 != 0):
            return 'NO'
    return str(count)
print(fairRations([1,2,3]))