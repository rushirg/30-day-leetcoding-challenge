"""
Week 4 - Problem 2
Bitwise AND of Numbers Range
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3308/
"""


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            n -= (n & -n)
        return n