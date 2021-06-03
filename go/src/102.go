func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return nil
	}

	res := [][]int{}
	queue := []*TreeNode{}

	queue = append(queue, root)
	for len(queue) != 0 {
		row := []int{}
		nextLevelQueue := []*TreeNode{}

		for _, node := range queue {
			row = append(row, node.Val)
			if node.Left != nil {
				nextLevelQueue = append(nextLevelQueue, node.Left)
			}
			if node.Right != nil {
				nextLevelQueue = append(nextLevelQueue, node.Right)
			}
		}

		res = append(res, row)
		queue = nextLevelQueue
	}

	return res
}