# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 06:11:43 2022

@author: Enj.Ammar
"""

class Solution:
    def longestCommonPrefix(strs: [str]) -> str:
        firstWord=strs[0]
        largestLength=len(firstWord)
        
        for i in range(len(strs)):
            word=strs[i]
            largestLength=min(largestLength,len(word))
            for k in range(largestLength):
                if firstWord[k]!=word[k]:
                    largestLength=k
                    break
        return firstWord[:largestLength]

                
            
        
    
if __name__=="__main__":
    
    strs = ["flower","flow","flight"]
    print(Solution.longestCommonPrefix(strs))