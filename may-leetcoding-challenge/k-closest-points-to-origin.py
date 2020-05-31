"""
Week 5 - Problem 2
K Closest Points to Origin
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3345/
"""
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        myDict = {}
        for i in range(len(points)):
            ans = (points[i][0])** 2 + (points[i][1])**2
            myDict[i] = ans
        myDict = {k: v for k, v in sorted(myDict.items(), key=lambda item: item[1])}
        result, count = [], 0
        for i in myDict:
            if count == K:
                break
            result.append(points[i])
            count += 1
        return(result)
