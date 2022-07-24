# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 03:15:46 2022

@author: Enj.Ammar
"""
import numpy as np

class Solution:
    def searchMatrixSlow(matrix: [[int]], target: int) -> bool:
        MMatrix=np.array(matrix)
        i=0
        n=len(matrix)
        m=len(matrix[0])
        while i < n:
            for j in range(m):
                current=MMatrix[i][j]
                if current>target:
                    MMatrix=np.delete(MMatrix, np.s_[j:], axis=1)  
                    n=len(MMatrix)
                    m=len(MMatrix[0])
                    i=0
                    break
                elif current==target:
                    return True
            if m==0:
                return False
            elif current<target:
                n-=1
                MMatrix=np.delete(MMatrix, np.s_[0], axis=0)                       
        return False
    
    
    def searchMatrixFast(matrix: [[int]], target: int) -> bool:
        
        i = len(matrix) - 1
        j = 0
        
        while True:
            if i < 0 or j >= len(matrix[0]):
                break
            current = matrix[i][j]
            if target < current:  # If target is smaller, go up
                i -= 1
            
            elif target > current: # If target is bigger, go right
                j += 1
            else:
                return True

        return False
        
    
if __name__=="__main__":
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    print(Solution.searchMatrixFast(matrix, target))