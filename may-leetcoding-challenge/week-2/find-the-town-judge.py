"""
Week 2 - Problem 3
Find the Town Judge
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3325/
"""


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        count = [0 for i in range(N + 1)]
        for tmp in trust:
            count[tmp[0]] -= 1
            count[tmp[1]] += 1

        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1
