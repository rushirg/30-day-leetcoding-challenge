"""
Week 3 - Problem 7
Leftmost Column with at Least a One
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3306/
"""


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        size = binaryMatrix.dimensions()
        rows, columns = size[0], size[1] - 1
        i, j = 0, columns
        ans = -1
        while (i < rows and j >= 0):
            if binaryMatrix.get(i, j) == 1:
                ans = j
                j -= 1
            else:
                i += 1
        return ans
