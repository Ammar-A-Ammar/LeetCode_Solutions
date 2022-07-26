# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 08:26:04 2022

@author: Enj.Ammar
"""

class Solution:
    def lengthOfLastWord(s: str) -> int:
        lastWordLength=0
        splitted=s.split()
        lastWord=splitted[-1]
        lastWordLength=len(lastWord)
        
        return lastWordLength
        


if __name__=="__main__":
    s = "luffy is still joyboy"
    print(Solution.lengthOfLastWord(s))