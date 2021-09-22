/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func flatten(root *TreeNode)  {
    var handler func(node *TreeNode)

	var next *TreeNode
	handler = func (node *TreeNode) {
		if node == nil {
			return
		}
		handler(node.Right)
		handler(node.Left)
		node.Right = next
		node.Left = nil
		next = node
	}
    handler(root)
}
