"""
Week 1 - Problem 4
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3286/
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
