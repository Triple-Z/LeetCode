/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}

	return recursion(root.Left, root.Right)
}

func recursion(left *TreeNode, right *TreeNode) bool {
	if left == nil && right == nil {
		return true
	} else if left == nil || right == nil {
		return false
	}

	if left.Val != right.Val {
		return false
	}

	return recursion(left.Left, right.Right) &&
		recursion(left.Right, right.Left)
}