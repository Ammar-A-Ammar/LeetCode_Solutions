# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 02:26:37 2022

@author: Enj.Ammar
"""

class Solution:
    def numMatchingSubseq( s: str, words:[str]) -> int:
        totalSum=0
        previous_index=0
        def isSubequenceWord(s,word):
             previous_index=0
             for i in range(len(word)):
                 try:
                     tmp=s.index(word[i],previous_index)
                     previous_index=tmp+1
                 except:
                     return False
             return True
         
        result=0
        for word in words:
            if isSubequenceWord(s, word):
                result+=1
        return result
            
         

        
                     
                 
            
        
        
if __name__=="__main__":
    s = "abcde"
    words = ["a","bb","acd","ace"]
    print(Solution.numMatchingSubseq(s,words))
