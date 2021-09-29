/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	// get A length
	lenA := 0
	for p := headA; p != nil; p = p.Next {
		lenA++
	}

	// get B length
	lenB := 0
	for q := headB; q != nil; q = q.Next {
		lenB++
	}

	diff := lenA - lenB
	p, q := headA, headB
	if diff < 0 {
		// B is longer than A
		diff = -diff
		for i := 0; i < diff; i++ {
			q = q.Next
		}
	} else {
		// A is longer than B
		for i := 0; i < diff; i++ {
			p = p.Next
		}
	}

	for p != nil && q != nil {
		if p == q {
			return p
		}
		p = p.Next
		q = q.Next
	}

	return nil

}