"""
Week 4 - Problem 1
Sort Characters By Frequency
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3337/
"""
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        result = ""
        s_counter = Counter(s)
        for k in s_counter.most_common():
            result += k[0] * k[1]
        return result
