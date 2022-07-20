# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 20:05:35 2022

@author: Enj.Ammar
"""

class Solution:
    def makesquare( matchsticks:[int]) -> bool:
        sumCount=0
        if sum(matchsticks)%4 !=0:
            return False
        
        squareLength=sum(matchsticks)/4
        
        i=0
        while i < len(matchsticks):
            if matchsticks[i]==squareLength:
                matchsticks=matchsticks[i+1:]
                i=0
            elif matchsticks[i]!=squareLength:
                sumCount+=matchsticks[i]
                i+=1
                
                if sumCount==squareLength:
                    matchsticks=matchsticks[i:]
                    i=0
                    sumCount=0
                elif sumCount>squareLength:
                    return False
            
        
        if len(matchsticks)==0:
            return True
        
        
        
if __name__=="__main__":  
    matchsticks = [5,5,5,5,4,4,4,4,3,3,3,3]
    print(Solution.makesquare(matchsticks))