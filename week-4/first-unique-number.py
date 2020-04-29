"""
Week 4 - Problem 7
First Unique Number
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3313/
"""


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.list= []
        self.dict = {}
        for i in nums: self.add(i)

    def showFirstUnique(self) -> int:
        while len(self.list) > 0 and self.dict[self.list[0]] > 1:
            self.list.pop(0)

        if len(self.list) == 0:
            return -1
        return self.list[0]


    def add(self, value: int) -> None:
        if value in self.dict:
            self.dict[value] += 1
        else:
            self.dict[value] = 1
            self.list.append(value)



# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)