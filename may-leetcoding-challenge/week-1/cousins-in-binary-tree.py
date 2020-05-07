"""
Week 1 - Problem 7
Cousins in Binary Tree
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3322/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        if root is None:
            return False

        queue = []
        dic = {}

        queue.append([root, None, 0])

        while(len(queue) > 0):

            node, parent, level = queue.pop(0)
            dic[node.val] = [parent, level]

            if node.left is not None:
                queue.append([node.left, node, level + 1])
            if node.right is not None:
                queue.append([node.right, node, level + 1])

        x_parent, x_level = dic[x][0], dic[x][1]
        y_parent, y_level = dic[y][0], dic[y][1]

        return x_level == y_level and x_parent != y_parent
