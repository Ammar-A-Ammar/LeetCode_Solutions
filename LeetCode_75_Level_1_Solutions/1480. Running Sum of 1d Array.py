# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 05:16:06 2022

@author: Enj.Ammar
"""

class Solution:
    def runningSum_1st_approach(nums: [int]) -> [int]:
        sumList=[]
        for i, number in enumerate (nums):
            number=sum(nums[0:i+1])
            sumList.append(number)
        return sumList

    def runningSum_2nd_approach(nums: [int]) -> [int]:
        sumList=[0]
        for number in nums:
            sumList.append(number+sumList[-1])
        sumList.remove(0)
        return sumList

if __name__ == "__main__":

    inputList=[0,1,2,3,4,5]
    print(Solution.runningSum_2nd_approach(inputList))
