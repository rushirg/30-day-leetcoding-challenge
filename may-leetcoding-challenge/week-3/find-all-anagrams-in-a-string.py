"""
Week 3 - Problem 3
Find All Anagrams in a String
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3332/
"""

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_len = len(p)
        p_c = Counter(p)
        result = []
        for i in range(len(s) - p_len + 1):
            if s[i] in p:
                tmp = s[i : i + p_len]
                tmp_c = Counter(tmp)
                if tmp_c == p_c:
                    result.append(i)
        return(result)
