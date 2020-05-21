"""
Week 3 - Problem 6
Kth Smallest Element in a BST
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3335/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        current = root
        stack = []
        count = 0
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
                continue
            elif stack:
                current = stack.pop()
                count += 1
                if count == k:
                    return current.val
                current = current.right
            else:
                break
