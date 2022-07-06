# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 06:41:36 2022

@author: Enj.Ammar
"""
class Solution:
    def get_fibonacci_naive(n:int):
        if n <= 1:
            return n
    
        previous = 0
        current  = 1
    
        for _ in range(n - 1):
            previous, current = current, previous + current
    
        return current 
    
    
    def get_fibonacci_fast(n:int):
         
        if n < 1 or n > 10**14 :
            return n

        previous = 0
        current  = 1
        period = [] #temporay period for fib mod m
        Full_period=[0,1] #adding 0 and 1 to make this the fullperiod

        for _ in range(n - 1):

            previous, current = current, (previous + current)   #looping and making the period
            if previous == 0 and current == 1 : #check if period is repeated to stop   
                Full_period.extend(period) # append the period to fullperiod 
                Full_period.pop(-1)        #''' when i print the full period i see that there is one more item from the next period so i pop 

                                           #   it out but even if i didnt pop it out,  it will not affect the result as the index will be right if minus from it 1 '''                          
                Fib_index= n%len(Full_period) #we get index by remaindering the n by the length of period
                return Full_period[Fib_index]  #we get the no. by acessing the list with the index we got then we return
            period.append(current)            #appending the result of looping in the period list

        return current #if it didnt match the if condition so it small and dont loop so we take the last item as it is the mod of fib


if __name__ == '__main__':
    
    n =  int(input())
    print(Solution.get_fibonacci_fast(n))
