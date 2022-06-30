# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 05:52:09 2022

@author: Enj.Ammar
"""

class Solution:
    def pivotIndex( nums: [int]) -> int:
        leftIndexSum=0
        rightIndexSum=0

        for i, number in enumerate (nums):
            leftIndexSum=sum(nums[0:i+1])
            rightIndexSum=sum(nums[i:])
            if leftIndexSum==rightIndexSum:
                return i
        return -1

if __name__ == "__main__":

    inputList=[1,7,3,6,5,6]
    print(Solution.pivotIndex(inputList))
