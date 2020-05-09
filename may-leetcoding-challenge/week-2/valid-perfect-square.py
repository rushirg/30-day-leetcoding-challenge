"""
Week 2 - Problem 2
Valid Perfect Square
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324/
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 0:
            return False
        s, i = 0, 1
        while s < num:
            s = s + i
            i += 2
        if s == num:
            return True
        return False
