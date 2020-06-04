"""
Week 1 - Problem 3
Two City Scheduling
https://leetcode.com/explore/featured/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3349/

Approach:
for ith person we find the savings he/she will make by visitng either city A or city B and store the difference in a
dictionary. Then sort these differences by values and select the first half index values from sorted list, which
indicate that they will go to city A, and the later half will go to city B

Note: The generated sorted list (order) is the index of the costs list
"""

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        totalCost = 0
        myDict = {}
        for i in range(len(costs)):
            myDict[i] = costs[i][0] - costs[i][1]
        order = sorted(myDict, key=myDict.get)
        for i in range(len(order)):
            if i < len(order)/2:
                totalCost += costs[order[i]][0]
            else:
                totalCost += costs[order[i]][1]
        return totalCost