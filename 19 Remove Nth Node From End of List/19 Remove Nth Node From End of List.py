"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        for _ in range(n):
            cur = cur.next
        if not cur:
            return head.next
        todelete = head
        prev, nxt = None, todelete.next
        while cur:
            cur = cur.next
            prev = todelete
            todelete = nxt
            nxt = nxt.next
        prev.next = nxt
        return head
