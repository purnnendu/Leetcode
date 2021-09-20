"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if(not root):   return []
        queue = collections.deque([root])
        all_levels = []
        while (queue):
            size = len(queue)
            curr_level = []
            for _ in range(size):
                curr = queue.popleft()
                curr_level.append(curr.val)
                if(curr.left):     queue.append(curr.left)
                if(curr.right):    queue.append(curr.right)
            all_levels.append(curr_level)
        return all_levels

        ## RECURSIVE APPROACH ##
        if not root:    return []
        levels = collections.defaultdict(list)
        def helper(node, level):
            levels[level].append(node.val)
            if node.left:   helper(node.left, level + 1)
            if node.right:  helper(node.right, level + 1)
        helper(root, 0)
        return levels.values()
