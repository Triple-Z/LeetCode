# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        list_len = 0
        if head:
            node = head.next
        else:
            return True
        
        while node:
            list_len += 1
            node = node.next
            
        stack = list()
        i = 0
        node = head
        while node:
            if i == list_len / 2:
                node = node.next
                i += 1
            elif list_len == 0 or i < list_len / 2:
                stack.append(node.val)
                node = node.next
                i += 1
            else:
                if node.val == stack.pop():
                    node = node.next
                    i += 1
                else:
                    return False
        
        return True
        