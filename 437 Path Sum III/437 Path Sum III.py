"""
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        res, sum_dic = 0, {0:1}
        def sum_from_root(root: TreeNode, sum_parent:int, sum_dic: dict) -> None:
            nonlocal res
            sum_parent += root.val
            k = sum_parent - targetSum
            if k in sum_dic:
                res += sum_dic[k]
            # add it to visit child
            if sum_parent in sum_dic:
                sum_dic[sum_parent] = sum_dic[sum_parent] + 1
            else:
                sum_dic[sum_parent] = 1
            if root.left != None:
                sum_from_root(root.left, sum_parent, sum_dic)
            if root.right != None:
                sum_from_root(root.right, sum_parent, sum_dic)
            # rollback dic
            sum_dic[sum_parent] = sum_dic[sum_parent] - 1

        sum_from_root(root, 0, sum_dic)
        return res
