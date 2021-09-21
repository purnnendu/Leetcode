"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i
        self.preorder_idx = 0
        def recurse(left, right):
            if left > right:
                return None
            root = TreeNode(preorder[self.preorder_idx])
            self.preorder_idx += 1
            root.left = recurse(left, inorder_map[root.val] - 1)
            root.right = recurse(inorder_map[root.val] + 1, right)
            return root
        return recurse(0, len(preorder) - 1)
