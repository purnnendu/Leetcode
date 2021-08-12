/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sortedArrayToBST(nums []int) *TreeNode {
    if len(nums) == 0 {
        return nil
    }
    return helper(nums, 0, len(nums)-1)
}

func helper(nums []int, left, right int) *TreeNode {
    if left > right {
        return nil
    }
    midpoint := (left + right) / 2
    node := &TreeNode{Val: nums[midpoint]}
    node.Left = helper(nums, left, midpoint-1)
    node.Right = helper(nums, midpoint+1, right)
    return node
}
