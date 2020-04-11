"""
Week 2 - Problem 4
Diameter of Binary Tree
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3293/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def depth(node):
            if not node:
                return 0
            left, right = depth(node.left), depth(node.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.ans
