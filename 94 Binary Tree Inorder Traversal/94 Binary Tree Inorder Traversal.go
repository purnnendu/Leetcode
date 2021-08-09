/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func inorderTraversal(root *TreeNode) []int {
    ans := []int{}

    var inorder func(*TreeNode)

    inorder = func(root *TreeNode) {
        if root == nil {return}

        inorder(root.Left)
        ans = append(ans, root.Val)
        inorder(root.Right)

    }
    inorder(root)

    return ans;
}
