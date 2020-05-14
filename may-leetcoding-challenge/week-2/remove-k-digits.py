"""
Week 2 - Problem 6
Remove K Digits
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3328/
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n, N, j = list(num), [], k
        for _ in range(len(num)-k):
            i = n.index(min(n[:j+1]))
            N.append(n[i])
            j -= i
            del n[:i+1]
        return "".join(N).lstrip("0") or "0"
