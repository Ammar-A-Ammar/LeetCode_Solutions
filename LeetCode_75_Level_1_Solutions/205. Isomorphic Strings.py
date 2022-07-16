# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 10:51:57 2022

@author: Enj.Ammar
"""

class Solution:
    def isIsomorphic(s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
# =============================================================================
#         stringList=[]
#         CHAR = 26
#         # for i in range(len(s)):
#         #     if s[i]==t[i]:
#         #         pass
#         #     else:
#         #         stringList.append(s[i])
#         #         stringList.append(t[i])
#         #         t=s.replace(t[i], s[i])    
#         
#         # if len(stringList) == len(set(stringList)) and s==t:
#         #     return True
#         # else:
#         #     return False
# =============================================================================
        
        
        
# =============================================================================
#         countChars1 = [0] * CHAR
#         countChars2 = [0] * CHAR
#           
#         # Process all characters one by one
#         for i in range(len(s)):
#             countChars1[ord(s[i]) - ord('a')] += 1
#             countChars2[ord(t[i]) - ord('a')] += 1
#           
#         # For string to be isomorphice the
#         # previous counts of appearances of
#         # current character in both string
#         # must be same if it is not same
#         # we return false
#         for i in range(len(s)):
#             if countChars1[ord(s[i]) - ord('a')] != countChars2[ord(t[i]) - ord('a')]:
#                 return False
#           
#         return True
# =============================================================================

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
                
if __name__=="__main__":
    s = "egg"

    t = "add"
    print(Solution.isIsomorphic(s, t))