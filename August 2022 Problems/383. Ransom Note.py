# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 13:02:00 2022

@author: Enj.Ammar
"""

class Solution:
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        i=0
        j=0
        if ransomNote in magazine:
            return True
        try:
            while i<len(ransomNote):
                while j<len(magazine):
                    if ransomNote[i]==magazine[j]:
                        ransomNote=ransomNote.replace(ransomNote[i],'',1)
                        magazine=magazine.replace(magazine[j],'',1)
                        j=0
                    else:
                        j+=1
                if len(ransomNote)==0:
                    return True
                else:
                    return False
        except:
            return True
                
        
        
        

if __name__=="__main__":
    ransomNote = "aab"
    magazine = "baa"
    print(Solution.canConstruct(ransomNote,magazine))