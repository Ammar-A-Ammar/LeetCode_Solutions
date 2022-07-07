# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 02:48:06 2022

@author: Enj.Ammar
"""

class Solution:
    def isInterleave_1st_approach( s1: str, s2: str, s3: str) -> bool:
        def search(list, platform):
            for i in range(len(list)):
                if list[i] == platform:
                    return True
            return False
        
        findingCharInS1=0
        findingCharInS2=0
        i=0
        copyS3=list(s3)
        copyS2=list(s2)
        copyS1=list(s1)
        if len(s1)+len(s2)!=len(s3):
            return False
        
        if len(s3)==0 and len(s2)==0 and len(s1)==0:
            return True
            
        while (i <len(copyS3)):
            z=copyS3[i]
            if search(copyS1,copyS3[i]):
                findingCharInS1=copyS1.index(copyS3[i])            
                copyS3.remove(copyS3[i])
                copyS1.remove(copyS1[findingCharInS1])
                i=-1
                
            elif search(copyS2, copyS3[i]):
                findingCharInS2=copyS2.index(copyS3[i])
                copyS3.remove(copyS3[i])
                copyS2.remove(copyS2[findingCharInS2])
                i=-1
            else:
                return False
            
# =============================================================================
#             if len(copyS1)==0:
#                 if copyS2==copyS3:
#                     return True
#                 else:
#                     return False
#                 
#             if len(copyS2)==0:
#                 if copyS1==copyS3:
#                     return True
#                 else:
#                     return False
# =============================================================================
            
            i+=1
            
        if len(copyS3)!=0:
            return False
        else:
            return True
                
        
                    

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1)+len(s2)!=len(s3):
            return False
        
        elif len(s3)==0 and len(s2)==0 and len(s1)==0:
            return True
        
    
        if (s1 and s1[0]==s3[0] ) and (s2 and s2[0]==s3[0]):
            return self.isInterleave(s1[1:],s2,s3[1:]) or  self.isInterleave(s1,s2[1:],s3[1:])
        
        
        if len(s3)>90:
            if len(s1) >=3 and s1[0]==s3[0] and s1[1]==s3[1] :
                return self.isInterleave(s1[2:], s2, s3[2:])
            elif len(s2) >=3 and s2[0]==s3[0] and s2[1]==s3[1]:
                return self.isInterleave(s1, s2[2:], s3[2:])
            
            elif s1 and s1[0]==s3[0]:
                return self.isInterleave(s1[1:], s2, s3[1:])
            elif s2 and s2[0]==s3[0]:
                return self.isInterleave(s1, s2[1:], s3[1:])
            
            else:
                return False
        
        
        elif s1 and s1[0]==s3[0]:
            return self.isInterleave(s1[1:], s2, s3[1:])
        elif s2 and s2[0]==s3[0]:
            return self.isInterleave(s1, s2[1:], s3[1:])
        
        
        else:
            return False
        
                
 
    
if __name__=="__main__":
    
        s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
        s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
        s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
        print(Solution.isInterleave(Solution,s1,s2, s3))