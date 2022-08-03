# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 11:22:34 2022

@author: Enj.Ammar
"""
from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.booking = SortedList()

    def book(self, start: int, end: int) -> bool:
        
        for oldStart, oldEnd in self.booking:
            if oldStart < end and start < oldEnd:
                return False
        self.booking.append((start, end))
        return True



if __name__=="__main__":
    myCalendar = MyCalendar()
    print(myCalendar.book(10, 20))
    print(myCalendar.book(15, 25))
    print(myCalendar.book(20, 30))
    