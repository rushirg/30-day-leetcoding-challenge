"""
Week 3 - Problem 4
Permutation in String
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3333/
"""
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len == 1:
            return s1 in s2

        s1_counter = Counter(s1)

        for i in range(s2_len - s1_len + 1):
            if s2[i] in s1_counter:
                tmp = s2[i:i + s1_len]
                tmp_counter = Counter(tmp)

                if tmp_counter == s1_counter:
                    return(True)
        return(False)
