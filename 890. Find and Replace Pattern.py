# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 21:22:29 2022

@author: Enj.Ammar
"""

class Solution:
    def findAndReplacePattern(words: [str], pattern: str) -> [str]:
        resultList=[]
        def isIsomorphic(s: str, t: str) -> bool:
            if len(s)!=len(t):
                return False
            charCount = dict()
            #initially setting c to "a"
            c = "a"
            #iterating over str1 and str2
            for i in range(len(s)):
                #if str1[i] is a key in charCount
                if s[i] in charCount:
                    c = charCount[s[i]]
                    if c != t[i]:
                        return False
                #if str2[i] is not a value in charCount
                elif t[i] not in charCount.values():
                    charCount[s[i]] = t[i]
                else:
                    return False
            return True
        for word in words:
            if isIsomorphic(word,pattern)==True:
                resultList.append(word)
                
        return resultList

if __name__=="__main__":
    words = ["abc","deq","mee","aqq","dkd","ccc"]
    pattern = "abb"
    print(Solution.findAndReplacePattern(words, pattern))