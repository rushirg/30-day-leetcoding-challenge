"""
Week 2 - Problem 1
876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3290/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        tmp = head
        while tmp is not None:
            count += 1
            tmp = tmp.next
        tmp = head
        for i in range(int(count / 2)):
            tmp = tmp.next
        return tmp
