"""
Week 3 - Problem 1
Product of Array Except Self
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3300/
"""
import numpy as np


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = list()
        product = np.prod(nums)
        zeroFlag = False
        if 0 in nums:
            zeroFlag = True
            zeroCount = nums.count(0)
            newNums = list(filter(lambda a: a != 0, nums))
            if not len(newNums) or zeroCount > 1:
                zeroProduct = 0
            else:
                zeroProduct = np.prod(newNums)
        for x in nums:
            if zeroFlag and x is not 0:
                val = 0
            elif x is 0:
                val = int(zeroProduct)
            else:
                val = int(product / x)
            ans.append(val)
        return ans
