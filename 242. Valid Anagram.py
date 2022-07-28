# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 16:59:13 2022

@author: Enj.Ammar
"""
from collections import Counter

class Solution:
    def isAnagramSlowApproach(s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
               
        sList=list(s.strip(" "))
        tList=list(t.strip(" "))
        try:
            i=0
            while i < len(tList):               
                tList.remove(sList[i])
                sList.remove(sList[i])
        except Exception:
            return False
            
        return True

    def isAnagramFasterApproach(s, t) :
        return sorted(s) == sorted(t)
        
    def isAnagramFastestApproach(s, t):
        s_counter=  Counter(s)
        t_counter = Counter(t)
        for c in s_counter:
            if s_counter[c] != t_counter[c]: return False
        return True

if __name__=="__main__":
    s = "anagram"
    t = "nagaram"
    print(Solution.isAnagramFastestApproach(s,t))