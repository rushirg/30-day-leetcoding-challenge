"""
Week 1 - Problem 2
Jewels and Stones
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/
"""


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        SDict = {}
        for ch in S:
            if ch in SDict:
                SDict[ch] += 1
            else:
                SDict[ch] = 1

        stones = 0

        for ch in J:
            if ch in SDict:
                stones += SDict[ch]

        return(stones)
