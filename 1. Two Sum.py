# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 04:57:04 2022

@author: Enj.Ammar
"""



class Solution:                
    def twoSum_1st_approach(nums, target) :
        for index1, number1 in enumerate (nums) :
            for index1, number1 in enumerate (nums) :
                for index2, number2 in enumerate (nums[index1+1:]) :
                    if number1+number2==target:
                            return [index1, index1+index2+1]
                    else:
                        continue
    def twoSum_2nd_approach( nums:[int], target: int):
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[j] + nums[i] == target:
                        return [i, j]
                
                
if __name__ == "__main__":
    # n=  input()
    inputList=[-1,-2,-3,-4,-5]

    target= -8
    
    print(Solution.twoSum_1st_approach(inputList, target))
    