/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
    a, b := headA, headB
    aLen, bLen := 0, 0
    for a.Next != nil || b.Next != nil {
        if a == b && aLen == bLen {
            return a
        }
        if a.Next != nil {
            a = a.Next
            aLen++
        }
        if b.Next != nil {
            b = b.Next
            bLen++
        }
    }
    if a != b {
        return nil
    }
    a, b = headA, headB
    for a.Next != nil {
        if a == b {
            return a
        }
        if (bLen - aLen > 0) {
            bLen--
            b = b.Next
        } else if (aLen - bLen > 0) {
            aLen--
            a = a.Next
        } else {
            a = a.Next
            b = b.Next
        }
    }
    return a
}
