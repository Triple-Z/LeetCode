# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        cur_1 = l1
        cur_2 = l2
        sum_1 = 0
        sum_2 = 0
        i = 0

        while cur_1:
            sum_1 += pow(10, i) * cur_1.val

            cur_1 = cur_1.next
            i += 1

        i = 0

        while cur_2:
            sum_2 += pow(10, i) * cur_2.val

            cur_2 = cur_2.next
            i += 1

        sum = sum_1 + sum_2

        # Create a new linked list
        head = ListNode(-1)
        length = len(str(sum))
        for i in range(1, length+1):
            if i == 1:
                head.val = int(str(sum)[length-i])
            elif i == 2:
                new_node = ListNode(int(str(sum)[length-i]))
                head.next = new_node
                last_node = new_node
            else:
                new_node = ListNode(int(str(sum)[length-i]))
                last_node.next = new_node
                last_node = new_node

        return head