"""
Week 1 - Problem 5
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3287/
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) < 2:
            return 0
        for i in range(1, len(prices)):
            value = prices[i] - prices[i-1]
            if value > 0:
                profit += value
        return profit

