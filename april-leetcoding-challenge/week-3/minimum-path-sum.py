"""
Week 3 - Problem 4
Minimum Path Sum
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3303/
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        tmp = [[0 for x in range(col)] for x in range(row)]

        prev = 0
        for c in range(col):
            tmp[0][c] = prev + grid[0][c]
            prev = tmp[0][c]

        prev = 0
        for r in range(row):
            tmp[r][0] = prev + grid[r][0]
            prev = tmp[r][0]

        for r in range(1, row):
            for c in range(1, col):
                tmp[r][c] = grid[r][c] + min(tmp[r - 1][c], tmp[r][c - 1])

        return tmp[r][c]
