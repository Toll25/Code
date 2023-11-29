#!/bin/python

def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(str(year) + ": leapyear")
        return True
    print(str(year) + ": normal year")
    return False


for i in range(0, 50000):
    isLeapYear(i)
