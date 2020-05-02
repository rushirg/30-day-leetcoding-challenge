"""
Week 4 - Problem 5
Longest Common Subsequence
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3311/
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mat = [[0 for c in range(len(text1) + 1)] for r in range(len(text2) + 1)]

        matI = 1
        for i in range(len(text2)):

            matJ = 1

            for j in range(len(text1)):
                if text2[i] == text1[j]:
                    mat[matI][matJ] = mat[matI - 1][matJ - 1] + 1
                else:
                    mat[matI][matJ] = max(mat[matI - 1][matJ], mat[matI][matJ - 1])
                matJ += 1
            matI += 1
        return(mat[len(text2)][len(text1)])
