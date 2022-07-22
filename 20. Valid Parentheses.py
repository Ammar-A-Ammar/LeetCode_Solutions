# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 12:53:10 2022

@author: Enj.Ammar
"""


class Solution:
    def isValid(s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == "{":
                stack.append(s[i])
            elif s[i] == "[":
                stack.append(s[i])
            elif s[i] == ')' and len(stack)!=0 and stack[-1]=='(' :
                stack.pop(-1)
            elif s[i] == "}" and len(stack)!=0 and stack[-1] == "{":
                stack.pop(-1)
            elif s[i] == "]" and len(stack)!=0 and stack[-1] == "[":
                stack.pop(-1)
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    s = "]"
    print(Solution.isValid(s))
