"""
Week 2 - Problem 3
Min Stack
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3292/
"""

# Approach 1:
import sys


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = sys.maxsize
        self.mytop = 0
        self.myList = list()

    def push(self, x: int) -> None:
        self.mytop = x
        if x < self.min:
            self.min = x
        self.myList.append(x)

    def pop(self) -> None:
        self.myList.pop()

    def top(self) -> int:
        return self.myList[-1]

    def getMin(self) -> int:
        return min(self.myList)


# Approach 2:
import sys


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.myList = list()
        self.myMinList = list()
        self.myMinList.append(sys.maxsize)

    def push(self, x: int) -> None:
        self.myList.append(x)
        if x <= self.myMinList[-1]:
            self.myMinList.append(x)

    def pop(self) -> None:
        if self.myList[-1] == self.myMinList[-1]:
            self.myMinList = self.myMinList[:-1]
        self.myList = self.myList[:-1]

    def top(self) -> int:
        return self.myList[-1]

    def getMin(self) -> int:
        return self.myMinList[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
