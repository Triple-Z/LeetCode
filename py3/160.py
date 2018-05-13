# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
	def getIntersectionNode(self, headA, headB):
		"""
		:type head1, head1: ListNode
		:rtype: ListNode
		"""
		p1, p2 = headA, headB
		len1, len2 = 1, 1
		while p1 != None and p2 != None:
			if p1 == p2:  # Intersect
				return p1
			else:
				p1 = p1.next
				len1 += 1
				p2 = p2.next
				len2 += 1

		while p1 != None:
			p1 = p1.next
			len1 += 1
		while p2 != None:
			p2 = p2.next
			len2 += 1
		
		# The second iteration
		diff = abs(len1 - len2)
		p1, p2 = headA, headB
		while p1 != None and p2 != None:
			if len1 >= len2 and diff > 0:
				p1 = p1.next
				diff -= 1
			elif len1 < len2 and diff > 0:
				p2 = p2.next
				diff -= 1
			else:  # find the intersection
				if p1 == p2:
					return p1
				else:
					p1 = p1.next
					p2 = p2.next
