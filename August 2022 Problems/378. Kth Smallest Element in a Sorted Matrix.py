# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 10:01:23 2022

@author: Enj.Ammar
"""


class Solution:
    def kthSmallest1stApproach( matrix: [[int]], k: int) -> int:
        return sorted(sum(matrix,[]))[k-1] 

    def kthSmallest2ndApproach( matrix: [[int]], k: int) -> int:
        temp = []
        for row in matrix:   #for i in range(len(matrix)):
            temp.extend(row) #temp = temp + matrix[i]
        temp.sort()
        return temp[k-1]


if __name__=="__main__":
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    print(Solution.kthSmallest2ndApproach(matrix,k))