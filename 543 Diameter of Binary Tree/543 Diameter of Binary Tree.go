/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
var runningMax = 0
func diameterOfBinaryTree(root *TreeNode) int {
    runningMax = 0
    dfs(root)
    return runningMax-1
}

func dfs(node *TreeNode) int {
    if node == nil {
        return 0
    }

    left := dfs(node.Left)
    right := dfs(node.Right)
    runningMax = max(runningMax, left+right+1)
    return max(left,right)+1
}

func max(val1 int, val2 int) int {
    if val1 >= val2 {
        return val1
    }
    return val2
}
