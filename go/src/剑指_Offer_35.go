/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
	if head == nil {
		return nil
	}

	var cur *Node = head
	var newHead Node = Node{}
	var newCur *Node = &newHead // dummy head

	nodeMap := make(map[*Node]*Node) // key: old node, value: new node

	// copy list
	for cur != nil {
		newNode := Node{
			Val:    cur.Val,
			Random: cur.Random,
		}
		newCur.Next = &newNode
		nodeMap[cur] = &newNode
		cur = cur.Next
		newCur = newCur.Next // to newNode
	}

	// reset random pointer for copied list
	newCur = newHead.Next
	for newCur != nil {
		newCur.Random = nodeMap[newCur.Random]
		newCur = newCur.Next
	}

	return newHead.Next

}