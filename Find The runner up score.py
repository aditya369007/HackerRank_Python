# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 18:03:13 2018

@author: adity
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maximum =max(arr)
    count_max = arr.count(maximum)
    for i in range(count_max):
        arr.remove(maximum)
        
    print(max(arr))
    
