# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 12:43:05 2022

@author: Enj.Ammar
"""

class Solution:
    def isSubsequence(s: str, t: str) -> bool:
        i=0
        sList=list(s)
        tList=list(t)
        if len(s)==0:
            return True
        
        while i < len(s) and len(tList)>i:
            if sList[i]==tList[i]:
                pass    
            else:
                tList.remove(tList[i])
                i-=1
            i+=1
            
        tList=tList[:i]
        if tList==sList:
            return True
        else :
            return False
        
if __name__=="__main__":
   s = "b"

   t ="abc"
   print(Solution.isSubsequence(s, t))