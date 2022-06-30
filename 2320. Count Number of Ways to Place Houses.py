# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 05:52:40 2022

@author: Enj.Ammar
"""

def countWays(n) :
    count1=1
    count2=1
    if (n == 1) :
        return 4
    

    for i in range(2,n+1) :
        prev_count2 = count2
        prev_count1 = count1
        count1 = prev_count2 + prev_count1
        count2 = prev_count1
    result = count1 + count2
    return (result*result)


# Driver program
if __name__ == "__main__":

	n = 3
	print ("Count of ways for ", n
		," sections is " ,countWays(n))
	
# This code is contributed by
# Chitranayal
