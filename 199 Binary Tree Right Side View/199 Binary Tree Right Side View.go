/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
var m []int
func rightSideView(root *TreeNode) []int {
    m = make([]int, 0)
    if root == nil {
        return nil
    }
    helper(root, 0)
    return m
}
func helper(root *TreeNode, depth int) {
    if root == nil {
        return
    }
    if len(m) <= depth {
        m = append(m, root.Val)
    }
    helper(root.Right, depth+1)
    helper(root.Left, depth+1)
}
