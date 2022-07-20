# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 02:03:49 2022

@author: Enj.Ammar
"""


class Solution:
    def romanToInt(s: str) -> int:

        totalSum=0
        i=0  
        while i < len(s):
                
            if s[i]=='I' and i<len(s)-1 and s[i+1]=="V":
                totalSum+=4
                i+=1
            elif s[i]=='I' and i<len(s)-1 and s[i+1]=="X":
                totalSum+=9
                i+=1
            elif s[i]=='X' and i<len(s)-1 and s[i+1]=="L":
                totalSum+=40
                i+=1
            elif s[i]=='X' and i<len(s)-1 and s[i+1]=="C":
                totalSum+=90
                i+=1
            elif s[i]=='C' and i<len(s)-1 and s[i+1]=="D":
                totalSum+=400
                i+=1
            elif s[i]=='C' and i<len(s)-1 and s[i+1]=="M":
                totalSum+=900
                i+=1
            elif s[i] =='I':
                totalSum+=1
            elif s[i]=='V':
                totalSum+=5
            elif s[i]=='X':
                totalSum+=10
            elif s[i]=='L':
                totalSum+=50
            elif s[i]=='C':
                totalSum+=100
            elif s[i]=='D':
                totalSum+=500
            elif s[i]=='M':
                totalSum+=1000
            i+=1
                
        return totalSum
if __name__=="__main__":
    s ="III"
    print(Solution.romanToInt(s))
