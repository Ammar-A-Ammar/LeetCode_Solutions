# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 17:19:01 2022

@author: Enj.Ammar
"""


class Solution:
    def searchRange(nums: [int], target: int) -> [int]:
        rangeIndex=[]
        try:
            startIndex=nums.index(target)
            rangeIndex.append(startIndex)
        except Exception:
            return [-1,-1]
        
        for i in range(startIndex,len(nums)):
            if nums[i]==target:
                continue
            elif nums[i]>target:
                rangeIndex.append(i-1)
                return rangeIndex
        return [startIndex,len(nums)-1]
            
  


if __name__=="__main__":
    nums = [2,2]
    target = 2
    print(Solution.searchRange(nums, target))