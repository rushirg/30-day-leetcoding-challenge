"""
Week 3 - Problem 6
Construct Binary Search Tree from Preorder Traversal
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3305/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        def constructBstInorder(preorder, inorder):
            preorder_length = len(preorder)

            if preorder is None or preorder_length is 0:
                return None

            root = TreeNode(preorder[0])
            root_index = inorder.index(root.val)

            root.left = constructBstInorder(preorder[1: root_index + 1], inorder[:root_index])
            root.right = constructBstInorder(preorder[root_index + 1: ], inorder[root_index + 1:])

            return root

        inorder = sorted(preorder)
        return constructBstInorder(preorder, inorder)
