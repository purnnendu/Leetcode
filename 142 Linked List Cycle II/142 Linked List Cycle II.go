/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func detectCycle(head *ListNode) *ListNode {
    slow, fast := head, head
    for fast!= nil && fast.Next!= nil{
        slow = slow.Next
        fast = fast.Next.Next
        if fast == slow {
            break
        }
    }
    if fast != slow || head == nil || head.Next == nil {
        return nil
    }
    count := 1
    curr := fast.Next
    for curr!= fast {
        curr = curr.Next
        count++
    }
	//count === len of the loop
    front,rear := head, head
    for i:=0;i<count;i++{
        front = front.Next //get a distance of L between them
    }
    for front!=rear { //keep moving both at same rate until they meet
        front = front.Next
        rear  = rear.Next
    }
    return rear //or front

}
