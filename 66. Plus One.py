# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 06:24:56 2022

@author: Enj.Ammar
"""

class Solution:
    def plusOne(digits: [int]) -> [int]:
        
        largeNumberString=''
        for number in digits:
            largeNumberString+=str(number)
            
        largeNumberInteger=int(largeNumberString)+1
        
        return [int(x) for x in str(largeNumberInteger)]
        
        
if __name__=="__main__":
    digits = [1,2,3]
    print(Solution.plusOne(digits))