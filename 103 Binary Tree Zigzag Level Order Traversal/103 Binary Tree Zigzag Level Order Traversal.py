"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ret = [[root.val]]
        level = [root]
        i = 1
        while(level):
            this_level = []
            for node in level:
                if node.left:
                    this_level.append(node.left)
                if node.right:
                    this_level.append(node.right)

            if this_level:
                if i % 2 == 0:
                    ret.append([node.val for node in this_level])
                else:
                    ret.append([node.val for node in this_level[::-1]])

            level = this_level
            i += 1

        return ret
