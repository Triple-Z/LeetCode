# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        prev = head
        cur = head.next
        while cur.next is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        cur.next = prev
        head.next = None
        
        return cur