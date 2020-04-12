"""
Week 2 - Problem 5
Last Stone Weight
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3297/
"""


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while True:
            if len(stones) <= 1:
                break
            max1 = max(stones)
            stones.remove(max1)
            max2 = max(stones)
            stones.remove(max2)

            if max2 <= max1:
                if max2 == max1:
                    continue
                elif max2 is not max1:
                    stones.append(abs(max1 - max2))
        return 0 if len(stones) == 0 else stones[0]
