# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 13:07:50 2022

@author: Enj.Ammar
"""

class Solution:
    def maximumUnits(boxTypes: [[int]], truckSize: int) :
        maxUnits=0
        boxTypes.sort(key=lambda row: (row[1], row[0]), reverse=True)
        
        for array in boxTypes:
            if array[0]<truckSize:
                maxUnits+=array[1]*array[0]
                truckSize-=array[0]
            else:
                maxUnits+=truckSize*array[1]
                break
        return maxUnits
                
            # if truckSize==0:
            #     break
                
                
                
                
                

if __name__ == "__main__":
    boxTypes=[[5,10],[2,5],[2,7],[3,9]]
    truckSize=10
    print(Solution.maximumUnits(boxTypes, truckSize))
    