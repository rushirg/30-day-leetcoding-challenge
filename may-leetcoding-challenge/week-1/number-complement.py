"""
Week 1 - Problem 4
Number Complement
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/
"""


import math
class Solution:
    def findComplement(self, num: int) -> int:
        return num ^ (2**(len(bin(num)) - 2) - 1)
