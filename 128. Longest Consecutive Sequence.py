# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 02:42:33 2022

@author: Enj.Ammar
"""

class Solution:
    def longestConsecutive(nums: [int]) -> int:
        LongestTemp=1
        consecutiveList=[]
        nums.sort()
        
        if len(nums)==0:
            return 0
        
        for i in range(1,len(nums)):     
            if nums[i]-1==nums[i-1]:
                LongestTemp+=1
            elif nums[i]==nums[i-1]:
                continue
            else:
                consecutiveList.append(LongestTemp)
                LongestTemp=1
                
        consecutiveList.append(LongestTemp)
        return max(consecutiveList)       
                
                
        
        
if __name__=="__main__":
    nums = [100,4,200,1,3,2]
    print(Solution.longestConsecutive(nums))