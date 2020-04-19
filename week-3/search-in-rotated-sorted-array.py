"""
Week 3 - Problem 5
Search in Rotated Sorted Array
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3304/
"""

# Method 1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        return -1


# Method 2
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def getIndex(nums, l, h, target):
            if l > h:
                return -1

            mid = int((l + h) / 2)
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if target >= nums[l] and target <= nums[mid]:
                    return getIndex(nums, l, mid - 1, target)
                return getIndex(nums, mid + 1, h, target)

            if target >= nums[mid] and target <= nums[h]:
                return getIndex(nums, mid + 1, h, target)
            return getIndex(nums, l, mid - 1, target)

        return getIndex(nums, 0, len(nums) - 1, target)
