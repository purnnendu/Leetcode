/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */

func connect(root *Node) *Node {
    if root == nil {
        return nil
    }
    queue := make([]*Node, 0)
    queue = append(queue, root)
    for len(queue) > 0 {
        l := len(queue)
        for i := 0; i < l; i++ { //iterate l elements only
            node := queue[0]
            queue = queue[1:]

            if i == l - 1 {
                node.Next = nil //last node in this level
            } else if i < l - 1 {
                node.Next = queue[0] //not the last node in this level
            }

            if node.Left != nil {
                queue = append(queue, node.Left)
            }
            if node.Right != nil {
                queue = append(queue, node.Right)
            }

        }
    }
    return root
}
