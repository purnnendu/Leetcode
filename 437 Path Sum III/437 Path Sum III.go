/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pathSum(root *TreeNode, targetSum int) int {
    if root == nil { return 0 }
    return dfs(root, []int{root.Val}, targetSum)
}

func dfs(node *TreeNode, nums []int, targetSum int) int {
    cnt := 0
    for i, sum := len(nums)-1, 0; i >= 0; i-- {
        sum += nums[i]
        if sum == targetSum { cnt++ }
    }
    if node.Left != nil { cnt += dfs(node.Left, append(nums, node.Left.Val), targetSum) }
    if node.Right != nil { cnt += dfs(node.Right, append(nums, node.Right.Val), targetSum) }
    return cnt
}
