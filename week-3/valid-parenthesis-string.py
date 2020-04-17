"""
Week 3 - Problem 2
Valid Parenthesis String
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3301/
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        for ch in s:
            low += 1 if ch == '(' else -1
            high += 1 if ch != ')' else -1
            if high < 0: break
            low = max(low, 0)
        return low == 0
