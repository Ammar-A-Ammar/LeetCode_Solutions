# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 13:41:31 2022

@author: Enj.Ammar
"""
from statistics import median as med

class Solution:
    def minMoves2_faild_approach(nums:[int]) -> int:
        diffList=[]
        totalMoves=0
        for i,number1 in enumerate(nums):
            for j,number2 in enumerate (nums[i+1:]):
                differnce=abs(number2-number1)
                diffList.append(differnce)
        minumumDifference=min(diffList)
        
        for i,number1 in enumerate(nums):
            for j,number2 in enumerate (nums[i+1:]):
                if abs(number2-number1)==minumumDifference:
                    minumumIndex=j+i
                    break
        minumumNumber=nums[minumumIndex]
        
        for number in nums:
            totalMoves+= abs(number-minumumNumber)
                
        return totalMoves
    
    def minMoves2_2nd_approach(nums:[int]) -> int:
        medianNumber=int(med(nums))
        totalMoves=0
        
        for number in nums:
            totalMoves+=abs(number-medianNumber)
           
        return totalMoves
        
        
        
if __name__ == "__main__":
    # n=  input()
    inputList=[1,3,2]
    print(Solution.minMoves2_2nd_approach(inputList))
    