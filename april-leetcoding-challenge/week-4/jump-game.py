"""
Week 4 - Problem 4
Jump Game
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3310/
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastIndex = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastIndex:
                lastIndex = i
        return lastIndex == 0
