"""
Week 4 - Problem 1
Subarray Sum Equals K
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3307/
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_t = defaultdict(int)
        hash_t[0] = 1
        cum_sum,count = 0, 0
        for num in nums:
            cum_sum += num
            count += hash_t[cum_sum-k]
            hash_t[cum_sum] = hash_t[cum_sum]+1
        return count
