/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
    var (
        result *Node = &Node{}
        p = result
        temp *Node = head
        nodes map[*Node]*Node = make(map[*Node]*Node, 0)
    )

    for temp != nil {
        p.Next = &Node{Val: temp.Val}

        nodes[temp] = p.Next

        p = p.Next
        temp = temp.Next
    }

    temp = head
    p = result.Next

    for temp != nil {
        if n, found := nodes[temp.Random]; found {
            p.Random = n
        }
        p = p.Next
        temp = temp.Next
    }

    return result.Next
}
