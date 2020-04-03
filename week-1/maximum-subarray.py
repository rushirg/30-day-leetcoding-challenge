"""
Week 1, Problem 3
https://leetcode.com/problems/maximum-subarray/
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3285/
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        curr_max = nums[0]
        for i in range(1, len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            max_so_far = max(curr_max, max_so_far)
        return max_so_far