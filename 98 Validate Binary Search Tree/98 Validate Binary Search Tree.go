/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidBST(root *TreeNode) bool {
    return RecValidate(root, nil, nil)
}

func RecValidate(n, min, max *TreeNode) bool {
    if n == nil {
        return true
    }
    if min != nil && n.Val <= min.Val {
        return false
    }
    if max != nil && n.Val >= max.Val {
        return false
    }
    return RecValidate(n.Left, min, n) && RecValidate(n.Right, n, max)
}
