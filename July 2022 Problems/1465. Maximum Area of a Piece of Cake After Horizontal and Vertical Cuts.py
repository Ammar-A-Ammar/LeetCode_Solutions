# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 00:38:11 2022

@author: Enj.Ammar
"""

class Solution:
    def maxArea(h: int, w: int, horizontalCuts:[int], verticalCuts:[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        maxWidth=max(verticalCuts[0],w-verticalCuts[-1])
        maxHeight=max(horizontalCuts[0],h-horizontalCuts[-1])
        
        
        if len(horizontalCuts)>1:
            for i in range(1,len(horizontalCuts)):
                maxHeight=max(maxHeight,horizontalCuts[i]-horizontalCuts[i-1])
                
        if len(verticalCuts)>1:
            for i in range(1,len(verticalCuts)):
                maxWidth=max(maxWidth,verticalCuts[i]-verticalCuts[i-1])
            

        
        
        return (maxWidth*maxHeight)% (10**9 + 7)
    
    
    
    
if __name__=="__main__":
    
    h = 5
    w = 4
    horizontalCuts = [3]
    verticalCuts = [3]
    print(Solution.maxArea(h, w, horizontalCuts, verticalCuts))
        