# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 22:34:40 2022

@author: Enj.Ammar
"""
import math 

class Solution:
    def isPowerOfThree(n: int) -> bool:
        if n==1 :
            return True
        elif n==0:
            return False
        
        x=n ** (1./3.)
        if x==3.0 or math.sqrt(n)==3.0:
            return True
        return False
        
        
        

if __name__=="__main__":
    n = 9
    print(Solution.isPowerOfThree(n))