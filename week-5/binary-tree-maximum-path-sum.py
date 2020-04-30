"""
Week 5 - Problem 1
Binary Tree Maximum Path Sum
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/532/week-5/3314/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -sys.maxsize - 1

        def findMaxSum(root):
            if root is None:
                return 0

            l = findMaxSum(root.left)
            r = findMaxSum(root.right)

            singleMax = max(max(l, r) + root.val, root.val)

            maxTop = max(singleMax, l + r + root.val)

            self.res = max(self.res, maxTop)

            return singleMax

        findMaxSum(root)
        return self.res
