# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 04:34:38 2022

@author: Enj.Ammar
"""

import numpy as np
def isX_Matrix(mat):
    N=len(mat)
    for number0 in mat:
        for index1, number1 in enumerate (mat) :
            for index2, number2 in enumerate (number1) :
                if index1==index2 :
                    if number1==0 or number2==0 :
                        return False
                if index1!=index2 :
                    if number1!=0 or number2!=0 :
                        return False
              
    return True             

def isX_Matrix2(mat):
    mylist=[]
    N=len(mat)
    diagnoal1=[]
    diagonal2=[]
    z=0
    for i in range(len(mat)):
      for j in range(len(mat[i])):
          mylist.append(mat[i][j])
          
    diagnoal1=[mat[i][i] for i in range(len(mat))]
    diagnoal2= [mat[i][len(mat)-i-1] for i in range(len(mat))]
    
    for number in diagnoal1:
        if number==0:
            return False
        
    for number in diagnoal2:
        if number==0:
            return False
        
        
    for number in mylist:
        if number!=0:
            z+=1
            
    if (N%2==0):
        if z==N*2:
            return True
        else:
            return False
    else:
        if z==N*2-1:
            return True
        else:
            return False
    

          
    # for i in range(0,N*N,N+z):
    #     z+=1 
    #     if mylist[i]==0:
    #         return False
       
    # for i in range(0,N*N):
    #     if i%4==0:
    #         continue
    #     if mylist[i]==0:
    #         return False
        
    
    # return True
    
          
           
                



if __name__ == "__main__":
    # n=  input()
    inputList=[[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]

    #target= -8
    
    print(isX_Matrix2(inputList))
    