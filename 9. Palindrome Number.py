# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 02:52:47 2022

@author: Enj.Ammar
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        for i in range(0,int(len(x)/2)):
            if x[i]!=x[len(x)-i-1]:
                return False
        return True
        
if __name__ == "__main__":
    x = 1
    print(Solution.isPalindrome(x))
        