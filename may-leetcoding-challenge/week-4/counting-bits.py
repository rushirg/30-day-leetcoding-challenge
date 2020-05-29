"""
Week 4 - Problem 7
Counting Bits
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3343/
"""


class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        if num is 0:
            return ans
        ans.append(1)
        if num is 1:
            return ans
        prevList = [1]
        while True:
            ans += prevList
            newList = [x + 1 for x in prevList]
            prevList = prevList + newList
            ans += newList
            if len(ans) > num:
                break
        return ans[:num + 1]
