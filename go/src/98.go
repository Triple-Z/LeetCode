func isValidBST(root *TreeNode) bool {
	return isValidSubBST(root, math.MinInt64, math.MaxInt64)
}

func isValidSubBST(root *TreeNode, lower, upper int) bool {
	if root == nil {
		return true
	}

	if root.Val <= lower || root.Val >= upper {
		return false
	}

	return isValidSubBST(root.Left, lower, root.Val) && isValidSubBST(root.Right, root.Val, upper)
}