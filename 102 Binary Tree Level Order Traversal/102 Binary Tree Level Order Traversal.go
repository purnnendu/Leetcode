/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
    res := [][]int{}
    traversal(root, 1, &res)
    return res
}

func traversal(root *TreeNode, level int, res *[][]int) {
    if root == nil {
        return
    }

    if len(*res) + 1 == level {
        row := []int{}
        *res = append(*res, row)
    }

    (*res)[level-1] = append((*res)[level-1], root.Val)

    traversal(root.Left, level+1, res)
    traversal(root.Right, level+1, res)
}
