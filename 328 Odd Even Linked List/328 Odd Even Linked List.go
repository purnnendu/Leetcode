/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func oddEvenList(head *ListNode) *ListNode {
    if head == nil || head.Next == nil || head.Next.Next == nil {
        return head
    }
    p := head
    p2 := head.Next
    head2 := head.Next
    for {
        var tmp, tmp2 * ListNode
        if p.Next != nil {
            tmp = p.Next.Next
        }
        if p2 != nil && p2.Next != nil {
            tmp2 = p2.Next.Next
        }
        if tmp != nil {
            p.Next = tmp
            p = p.Next
        } else {
            p.Next = head2
            break
        }
        p2.Next = tmp2
        p2 = p2.Next
    }
    return head
}
