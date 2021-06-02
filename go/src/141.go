func hasCycle(head *ListNode) bool {
	if head == nil {
		return false
	}

	fast := head.Next
	slow := head

	for fast != nil && slow != nil {
		if fast != slow {
			if fast.Next != nil {
				fast = fast.Next.Next
			} else {
				return false
			}
			slow = slow.Next
		} else {
			return true
		}
	}

	return false
}