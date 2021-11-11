func verifyPostorder(postorder []int) bool {
	if len(postorder) == 0 {
		return true
	}

	rootIdx := len(postorder) - 1
	rightIdx := 0
	for ; rightIdx < rootIdx; rightIdx++ {
		if postorder[rightIdx] > postorder[rootIdx] {
			break
		}
	}
	// left sub-tree: [0:rightIdx)
	// right sub-tree: [rightIdx:rootIdx)
	for i := rightIdx; i < rootIdx; i++ {
		if postorder[i] < postorder[rootIdx] {
			// invalid right sub-tree node
			return false
		}
	}

	return verifyPostorder(postorder[:rightIdx]) && // left sub-tree
		verifyPostorder(postorder[rightIdx:rootIdx])
}