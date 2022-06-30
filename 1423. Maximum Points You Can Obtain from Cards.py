# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 04:24:36 2022

@author: Enj.Ammar
"""

class Solution:
    def maxScore(cardPoints:[int], k: int) -> int:
        sumLeft=0
        sumRight=0
        tempList=[]
        superMax=0
        for number in cardPoints[0:k]:
            sumLeft+=number
            tempList.append(number)
        for number in cardPoints[len(cardPoints)-k:len(cardPoints)]:
            tempList.append(number)
            sumRight+=number
            
        for i in range(3):
            superMax+=max(tempList)
            maxpos = tempList.index(max(tempList))
            del tempList[maxpos]
        
        return superMax
    
    
    def maxGreedyScore(cardPoints:[int], k: int) -> int:
        Left=0
        Right=0
        tempList=[]
        superMax=0
        for i in range(k):
            if cardPoints[0]>cardPoints[-1]:
                superMax+=cardPoints[0]
                del cardPoints[0]
            else:
                superMax+=cardPoints[-1]
                del cardPoints[-1]
        return superMax
        
        


if __name__ == "__main__":
    # n=  input()
    nums =[100,40,17,9,73,75]
    k = 3
    print(Solution.maxScore(nums,k))