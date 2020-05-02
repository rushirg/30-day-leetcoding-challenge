"""
Week 5 - Problem 2
Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/532/week-5/3315/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:


        def checkPath(root, arr, n, index):
            if not root or index == n:
                return False

            if not root.left and not root.right:
                if root.val == arr[index] and index == n-1:
                    return True
                return False

            return ((index < n) and (root.val == arr[index]) and (checkPath(root.left, arr, n, index+1) or checkPath(root.right, arr, n, index+1)))


        if not root:
            return len(arr) == 0
        return checkPath(root, arr, len(arr), 0)

