"""
Week 2 - Problem 1
Check If It Is a Straight Line
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3323/
"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        def slope(x1, y1, x2, y2):
            if x1 == x2 or y1 == y2:
                return False
            else:
                return (x2 - x1) / (y2 - y1)


        # if less than two points or no points
        if len(coordinates) < 2:
            return False

        # if only two points
        if len(coordinates) == 2:
            return True

        # if more than two points
        myslope = slope(coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1])

        prevX, prevY = coordinates[0][0], coordinates[0][1]

        for i in range(1, len(coordinates)):
            temp_slope = slope(prevX, prevY, coordinates[i][0], coordinates[i][1])
            if myslope != temp_slope:
                return False
            prevX, prevY = coordinates[i][0], coordinates[i][1]
        return True
