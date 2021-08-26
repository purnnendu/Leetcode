/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) (head *ListNode) {

    head = l1
    var previous *ListNode
    carry := 0

	for l1 != nil || l2 != nil {

        d1, d2 := 0, 0

        if l1 != nil {
            d1 = l1.Val
        }else{
            previous.Next = &ListNode{Val: 0}
            l1 = previous.Next
        }

        if l2 != nil {
            d2 = l2.Val
            l2 = l2.Next
        }

        sum := d1 + d2 + carry
        sum, carry = sum % 10, sum / 10

        l1.Val = sum
        previous = l1
        l1 = l1.Next
	}

    if carry > 0 {
        previous.Next = &ListNode{Val: carry}
    }

	return
}
