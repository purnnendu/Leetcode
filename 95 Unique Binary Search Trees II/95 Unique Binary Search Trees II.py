"""
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:

Input: n = 1
Output: [[1]]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(left,right):

            if (left,right) in memo:
                return memo[(left,right)]

            if left > right:
                return [None]

            if left == right:
                return [TreeNode(left)]

            trees = []
            for i in range(left,right+1):

                left_subtrees = helper(left, i-1)
                right_subtrees = helper(i+1, right)

                for lst in left_subtrees:
                    for rst in right_subtrees:
                        root = TreeNode(i)
                        root.left = lst
                        root.right = rst
                        trees.append(root)

            memo[(left,right)] = trees
            return trees

        memo = {}
        return helper(1, n)
