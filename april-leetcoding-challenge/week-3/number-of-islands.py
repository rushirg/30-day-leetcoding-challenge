"""
Week 3 - Problem 3
Number of Islands
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3302/
"""


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
                return 0

            grid[i][j] = '0'
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)
            return 1

        if grid is None or len(grid) is 0:
                return 0
        islandsCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    islandsCount += dfs(grid, i, j)
        return islandsCount
