"""
Week 1 Problem 1
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3283/
https://leetcode.com/problems/single-number/
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            ans ^= x
        return ans
