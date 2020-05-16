"""
Week 3 - Problem 1
Maximum Sum Circular Subarray
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3330/
"""


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if len(A) == 1:
            return A[0]

        max_so_far = A[0]
        curr_max = A[0]
        min_so_far = A[0]
        curr_min = A[0]
        total = A[0]

        for i in range(1, len(A)):
            curr_max = max(A[i], curr_max + A[i])
            max_so_far = max(max_so_far, curr_max)

            curr_min = min(A[i], curr_min + A[i])
            min_so_far = min(min_so_far, curr_min)
            total += A[i]

        if min_so_far == total:
            return max_so_far

        return max(max_so_far, total - min_so_far)
