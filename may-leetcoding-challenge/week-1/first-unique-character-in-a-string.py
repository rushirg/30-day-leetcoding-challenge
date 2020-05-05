"""
Week 1 - Problem 5
First Unique Character in a String
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/
"""
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        string_counter = Counter(s)

        for i in range(len(s)):
            if string_counter[s[i]] == 1:
                return i
        return -1
