"""
Week 4 - Problem 3
LRU Cache
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3309/
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = {}

    def get(self, key: int) -> int:
        val = -1
        if key in self.values:
            val =  self.values.pop(key)
            self.values[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.values.pop(key)
            self.values[key] = value
        elif self.capacity > len(self.values):
            self.values[key] = value
        else:
            remove_val = list(self.values.keys())[0]
            self.values.pop(remove_val)
            self.values[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)