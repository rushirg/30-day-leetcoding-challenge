"""
Week 1 - Problem 1
First Bad Version
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3316/
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n is None:
            return n

        l, r = 1, n
        while l < r:
            mid = int((l + r) / 2)
            if isBadVersion(mid):
                r = mid
            else:
                if mid == l:
                    return r
                l = mid
        return r
