"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node_1, node_2):
            if node_1 is None and node_2 is None:
                return True

            if node_1 is None or node_2 is None:
                return False

            return node_1.val == node_2.val and helper(node_1.left, node_2.right) and helper(node_1.right, node_2.left)
        return helper(root, root)
