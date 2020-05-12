"""
Week 2 - Problem 4
Flood Fill
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3326/
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        def fill(image, sr, sc, newColor, color):
            if(sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != color):
                return

            image[sr][sc] = newColor

            fill(image, sr - 1, sc, newColor, color)
            fill(image, sr + 1, sc, newColor, color)
            fill(image, sr, sc - 1, newColor, color)
            fill(image, sr, sc + 1, newColor, color)

        if image[sr][sc] == newColor:
            return image
        fill(image, sr, sc, newColor, image[sr][sc])
        return image
