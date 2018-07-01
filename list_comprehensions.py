# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 17:59:51 2018

@author: adity
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    count = 0
    print('[',end="",flush=True)
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                if ((i+j+k) != n):
                    print([i,j,k], end="",flush=True)
                count = count + 1
                if((count<((x+1)*(y+1)*(z+1))) and (i+j+k) != n):
                    print(', ', end="",flush=True)
                        
    print(']',end="",flush=True)