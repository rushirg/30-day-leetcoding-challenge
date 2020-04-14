"""
Week 2 - Problem 6
Contiguous Array
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3298/
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mydict = {0: -1}
        maxlen = count = 0

        for i in range(len(nums)):
            if nums[i] is 1:
                count += 1
            else:
                count -= 1
            if count in mydict:
                maxlen = max(maxlen, i - mydict[count])
            else:
                mydict[count] = i

        return(maxlen)

