# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        p1, p2 = l1, l2
        # dummy head
        head = ListNode()
        cur = head

        while p1 and p2:
            if p1.val <= p2.val:
                # use l1 node
                cur.next = p1
                p1 = p1.next
            else:
                # use l2 node
                cur.next = p2
                p2 = p2.next

            cur = cur.next

        if p1:
            cur.next = p1
        elif p2:
            cur.next = p2
        
        return head.next

