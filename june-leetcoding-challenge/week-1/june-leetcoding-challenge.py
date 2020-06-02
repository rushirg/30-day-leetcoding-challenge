"""
Week 1 - Problem 2
Delete Node in a Linked List
https://leetcode.com/explore/featured/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3348/

Idea:
Given the conditions that the linked list will atlest have two nodes, all the node values will be unique,
and also the given node will not be tail node. We can achieve the delete operation by just copying next node
data to the current node and pointing the current node's next pointer to the node after the next node (may be None/Null)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next