/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    var cur,next,prev *ListNode
    cur = head
    for (cur != nil){
        next = cur.Next  // saving the next point
        cur.Next = prev // changing it previous
        prev = cur // setting previous to current
        cur = next //setting next to current
    }
    return prev
}
