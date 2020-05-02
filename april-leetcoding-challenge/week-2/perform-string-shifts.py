"""
Week 2 - Problem 7
Perform String Shifts
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3299/
"""


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for ops in shift:
            direction = ops[0]
            amount = ops[1]
            if direction is 0:
                s = s[amount:] + s[:amount]
            else:
                length = len(s)
                for i in range(1, amount + 1):
                    s = s[-1] + s[:length - 1]
        return(s)
