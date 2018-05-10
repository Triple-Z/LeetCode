# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		p1, p2 = l1, l2
		new_head = None

		while p1 != None and p2 != None:
			if p1.val > p2.val:
				if p1 == l1 and p2 == l2:
					new_head = ListNode(p2.val)
					p2 = p2.next
					last_node = new_head
				else:
					new_node = ListNode(p2.val)
					last_node.next = new_node
					p2 = p2.next
					last_node = new_node
			else:
				# p1.val < p2.val
				if p1 == l1 and p2 == l2:
					new_head = ListNode(p1.val)
					p1 = p1.next
					last_node = new_head
				else:
					new_node = ListNode(p1.val)
					last_node.next = new_node
					p1 = p1.next
					last_node = new_node
		
		if p1 != None:
			while p1 != None:
				if new_head is None:
					new_head = ListNode(p1.val)
					p1 = p1.next
					last_node = new_head
				else:
					new_node = ListNode(p1.val)
					last_node.next = new_node
					p1 = p1.next
					last_node = new_node

		elif p2 != None:
			while p2 != None:
				if new_head is None:
					new_head = ListNode(p2.val)
					p2 = p2.next
					last_node = new_head
				else:
					new_node = ListNode(p2.val)
					last_node.next = new_node
					p2 = p2.next
					last_node = new_node

		return new_head
