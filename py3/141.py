# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head is None:
            return False

        p_slow, p_fast = head, head.next

        while p_fast is not None and p_fast != p_slow:
            p_fast = p_fast.next
            if p_fast is not None:
                p_fast = p_fast.next
            else:
                break
            p_slow = p_slow.next

        if p_fast is None:
            return False
        else:
            return True
