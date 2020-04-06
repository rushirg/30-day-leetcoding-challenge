"""
Week 1 - Problem 6
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3288/
"""
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            ans[str(sorted(word))].append(word)
        return(list(ans.values()))