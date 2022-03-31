"""
Problem no.6:
    Given a year, determine whether it is a leap year.
    If it is a leap year, return the Boolean True, otherwise
    return False.
Link: https://www.hackerrank.com/challenges/write-a-function/
"""

def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

year = int(input())
print(is_leap(year))
