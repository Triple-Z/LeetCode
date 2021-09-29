/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	p, q := l1, l2
	var dummyHead *ListNode = &ListNode{}
	cur := dummyHead

	for p != nil && q != nil {
		if p.Val <= q.Val {
			// use p
			cur.Next = p
			p = p.Next
		} else {
			// use q
			cur.Next = q
			q = q.Next
		}
		cur = cur.Next
	}

	if p != nil {
		cur.Next = p
	}

	if q != nil {
		cur.Next = q
	}

	return dummyHead.Next
}