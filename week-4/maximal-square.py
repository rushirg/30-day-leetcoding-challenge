"""
Week 4 - Problem 6
Maximal Square
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3312/
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        temp_matrix = [[0 for c in range(cols + 1)] for r in range(rows + 1)]
        max_ele = 0

        for r in range(1, len(temp_matrix)):
            for c in range(1, len(temp_matrix[0])):
                if int(matrix[r - 1][c - 1]) == 1:
                    temp_matrix[r][c] = min(
                        temp_matrix[r - 1][c - 1], min(temp_matrix[r - 1][c], temp_matrix[r][c - 1])) + 1
                    max_ele = max(max_ele, temp_matrix[r][c])

        return(max_ele * max_ele)
