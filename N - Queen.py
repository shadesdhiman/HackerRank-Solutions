# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 20:30:35 2021

@author: Dhiman
"""

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    top = n - r_q 
    print("top", top)
    
    down = r_q-1
    print("Down", down)
    
    left = c_q-1
    print("Left", left)
    
    right = n - c_q
    print("right", right)
    
    #  top - left
    topleft = min(top, left)
    print("topleft", topleft)
    
    #bottom left
    bottomleft = min(left, down)
    print("bottomleft", bottomleft)
    
    #bottom right
    bottomright = min(down, right)
    print("Bottomright", bottomright)
    
    topright = min(right, top)
    print("topright", topright)
    
    #obstacles
    for i in obstacles:
        
        row = i[0]
        col = i[1]
        print(r_q,c_q, row,col)
        
        #left
        if row == r_q and col < c_q :
            print("*")
            if  c_q - col-1 < left:
                left = c_q - col - 1
                print("left after obs", left)
                
        #right
        elif row == r_q and col >c_q:
            
            if col - c_q-1 < right:
                right = col-c_q-1
                print("right after obs", right)
        #up
        elif row > r_q and col == c_q:
            if row - r_q -1 < top:
                top = row - r_q -1
                print("top after obs", top)
        #down        
        elif row< r_q and col == c_q:
            if r_q - row-1 < down:
                down = r_q - row -1
                print("down after obs", down)
        #top left
        elif row > r_q and col < c_q:
            if row - r_q == c_q - col:
                if row - r_q -1< topleft:
                    topleft = row - r_q -1
                    print("top left after obs", topleft)
        #bottom left
        elif row< r_q and col < c_q:
            if  r_q - row ==  c_q-col:
                if r_q - row -  1 < bottomleft:
                    bottomleft  = r_q - row - 1
                    print("bottom left after obs ", bottomleft)
        # top right
        elif row > r_q and col > c_q:
            if row - r_q == col - c_q:
                if row - r_q -1 < topright:
                    topright = row - r_q -1
                    print("topright after obs", topright)
        #bottom tight
        elif row < r_q and col > c_q:
            if r_q - row == col - c_q:
                if r_q - row-1< bottomright:
                    bottomright = r_q - row-1
                    print("bottom right after obs", bottomright)
        
    return (top + left + right + down + topleft + topright + bottomleft + bottomright)
        
        
            
        
    
    
    
    
    
    
    

    
    
print(queensAttack(8, 3, 4,4, [[3,5],[3,4],[3,3],[4,3],[5,3],[5,4],[5,5],[4,5]]))
