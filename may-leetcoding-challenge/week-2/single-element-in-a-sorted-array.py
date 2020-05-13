"""
Week 2 - Problem 5
Single Element in a Sorted Array
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3327/
"""

"""
Method 1 (Simple):
Time Complexity: O(n)
"""

nums = []
result = 0
for n in nums:
    result = result ^ n
print(result)


"""
Method 2:
Time Complexity: O(log n)
"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        def find(nums, left, right):

            if left > right:
                return None

            if nums[left] == nums[right]:
                return nums[left]

            mid = (left + right) // 2

            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    return find(nums, mid + 2, right)
                else:
                    return find(nums, left, mid)
            else:
                if nums[mid] == nums[mid - 1]:
                    return find(nums, mid + 1, right)
                else:
                    return find(nums, left, mid - 1)

        return find(nums, 0, len(nums) - 1)
