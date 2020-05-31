"""
Week 5 - Problem 3
Edit Distance
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3346/
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_word1 = len(word1)
        len_word2 = len(word2)
        matrix = [[0 for x in range(len_word1 + 1)] for x in range(len_word2 + 1)]

        for i in range(len_word1 + 1):
            matrix[0][i] = i

        for i in range(len_word2 + 1):
            matrix[i][0] = i


        for i in range(1, len_word2 + 1):
            for j in range(1, len_word1 + 1):
                if word2[i - 1] == word1[j - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1]
                else:
                    matrix[i][j] = 1 + min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1])
        return matrix[-1][-1]
