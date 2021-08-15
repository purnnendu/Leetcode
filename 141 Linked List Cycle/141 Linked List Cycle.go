/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
    if head == nil {
        return false
    }

    if head.Next == nil {
        return false
    }

    ch1 := head
    ch2 := head

    for {
        ch1 = ch1.Next
        ch2 = ch2.Next.Next

        if ch2 == nil || ch2.Next == nil {
            return false
        }

        if ch1 == ch2 {
            return true
        }
    }
}

func hasCycleSimple(head *ListNode) bool {
    if head == nil {
        return false
    }
    m := map[*ListNode]bool{}
    m[head] = true
    n := head
    for {
        n = n.Next
        if n == nil {
            return false
        }
        if m[n] {
            return true
        }
        m[n]=true
    }
}
