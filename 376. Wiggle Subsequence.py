# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 02:33:34 2022

@author: Enj.Ammar
"""

class Solution:
    def wiggleMaxLength( nums: [int]) -> int:
        postive=1
        negative=1
        
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>0:
                postive=1+negative
            elif nums[i]-nums[i-1]<0:
                negative=1+postive
        return max(postive,negative)
    
if __name__=="__main__":
    
    nums = [1,5,7,10,15,17]
    print(Solution.wiggleMaxLength(nums))