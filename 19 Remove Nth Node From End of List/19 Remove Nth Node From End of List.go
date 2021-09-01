/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    var cur, cur2 *ListNode
	cur = head
	cur2 = head
	if head.Next == nil && n == 1 {
		return nil
	}
	if n == 1 {
		for {
			if cur.Next == nil {
				break
			}
			cur2 = cur
			cur = cur.Next
		}
		cur2.Next = nil
		return head
	} else {
		i := 0
		for ; ; i++ {
			if cur.Next == nil {
				break
			}
			cur = cur.Next
			if i >= n {
				cur2 = cur2.Next
			}
		}
		if i+1 == n {
			head = head.Next
			return head
		} else {
			cur2.Next = cur2.Next.Next
			return head
		}
    }
}
