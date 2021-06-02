func reverseList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	previous := head
	cur := previous.Next

	head.Next = nil
	for cur != nil {
		next := cur.Next
		cur.Next = previous
		previous = cur
		cur = next
	}

	return previous
}