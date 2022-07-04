# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 01:06:42 2022

@author: Enj.Ammar
"""

class Solution:
    def candyFailed(ratings: [int]) -> int:
        MinmumCandy=len(ratings)
        if len(ratings)>1:
            for i in range(1,len(ratings)-1,2):
                if ratings[i]>=ratings[i+1] or ratings[i]>=ratings[i-1]:
                    MinmumCandy+=1
                    
            
            if ratings[0]>ratings[1]:
                MinmumCandy+=1
            
            if ratings[-1]>ratings[len(ratings)-2]:
                MinmumCandy+=1
                    
            return MinmumCandy
        else:
            return len(MinmumCandy)
        
    def candy(ratings: [int]) -> int:
        candyList=[1]*len(ratings)
        
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1] and candyList[i]<=candyList[i-1]:
                candyList[i]=candyList[i-1]+1
                
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1] and candyList[i]<=candyList[i+1]:
                candyList[i]=candyList[i+1]+1
                
                
        return sum(candyList)
            
    
if __name__=="__main__":
    
      ratings = [1,2,87,87,87,2,1]
      print(Solution.candy(ratings))