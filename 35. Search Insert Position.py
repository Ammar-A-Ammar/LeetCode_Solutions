# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 08:45:46 2022

@author: Enj.Ammar
"""

class Solution:
    def searchInsert(self, nums:[int], target: int) -> int:
        i=len(nums)
        # Edge case: length is 0 and target matches or is smaller than only element
        if((i == 1 and target <= nums[0]) or i==0):
            return 0

        # Edge case: target > larget element
        if(target > nums[-1]):
            return i
        
        
        # Divide and conquer
        median=int(i/2)
        currNumber=nums[median]
        
        if currNumber==target:
            return median
        elif currNumber>target:       
            return Solution.searchInsert(0,nums[:median],target)
        elif currNumber<target: 
            return 1+median+Solution.searchInsert(0,nums[median+1:],target)
           
            
                
    
        
        
if __name__=="__main__":
    nums = [1,3,5]
    target = 4
    print(Solution.searchInsert(0,nums, target))