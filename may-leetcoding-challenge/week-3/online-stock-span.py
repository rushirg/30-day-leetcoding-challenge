"""
Week 3 - Problem 5
Online Stock Span
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3334/
"""

class StockSpanner:

    def __init__(self):
        self.myList = []

    def next(self, price: int) -> int:
        price_val, price_span = price, 1

        while (self.myList and self.myList[-1][0] <= price_val):
            old_price_val, old_price_span = self.myList.pop()
            price_span += old_price_span
        self.myList.append((price_val, price_span))
        return price_span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
