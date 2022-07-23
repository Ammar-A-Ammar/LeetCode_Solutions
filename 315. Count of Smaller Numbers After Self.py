# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 16:42:45 2022

@author: Enj.Ammar
"""

from sortedcontainers import SortedList

class Solution:
    def countSmallerSlow(nums: [int]) -> [int]:
        resultList=[]
        count=0
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]<nums[i]:
                    count+=1
            resultList.append(count)
            count=0
        return resultList
    
    
    def countSmallerFaster(nums):
        resultList=[]
        sorted_List=SortedList(nums)
        
        for number in nums:
            index=sorted_List.index(number)
            resultList.append(index)
            sorted_List.remove(number)
        return resultList

if __name__ == "__main__":
    nums = [5,2,6,1]
    print(Solution.countSmallerFaster(nums))
