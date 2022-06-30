# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 04:57:04 2022

@author: Enj.Ammar
"""

class Solution:
    def checkPossibility(nums: [int]):
        numberOfChnages=0
        leg=len(nums)
        for index1,number1 in enumerate (nums):
            if index1+1==len(nums):
                break
            number2 = nums[index1+1]
            if number2<number1:
                numberOfChnages+=1
            else :
                if len(nums)>=4:
                    if index1-2 >= 0 and index1+1<len(nums) and nums[index1-2]>number1 and nums[index1-1]>nums[index1+1] :
                        numberOfChnages+=5 
                        break
                    else :
                        continue
                continue
            
            
                    
        if numberOfChnages>1:
            return False
        else:
            return True
                
                
if __name__ == "__main__":
    # n=  input()
    nums =[3,4,2,3]
    
    print(Solution.checkPossibility(nums))