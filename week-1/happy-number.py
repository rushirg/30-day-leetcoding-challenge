"""
202. Happy Number
https://leetcode.com/problems/happy-number/
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3284/
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        tmpset = set()
        while(True):
            tmp = 0
            for i in range(len(n)):
                tmp += int(n[i]) ** 2
            n = str(tmp)
            if n in tmpset:
                return False
            tmpset.add(n)
            if tmp is 1:
                return True

