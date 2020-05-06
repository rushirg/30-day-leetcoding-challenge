"""
Week 1 - Problem 6
Majority Element
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        major = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == major:
                count += 1
            else:
                count -= 1
                if count == 0:
                    major = nums[i]
                    count = 1
        return major
