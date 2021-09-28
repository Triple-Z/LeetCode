/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSubStructure(A *TreeNode, B *TreeNode) bool {
	if A == nil || B == nil {
		return false
	}

	if A.Val == B.Val && isSame(A, B) {
		return true
	}

	if isSubStructure(A.Left, B) {
		return true
	}

	if isSubStructure(A.Right, B) {
		return true
	}

	return false
}

func isSame(a *TreeNode, b *TreeNode) bool {
	if b == nil {
		return true
	}

	if a == nil {
		return false
	}

	if a.Val != b.Val {
		return false
	}

	return isSame(a.Left, b.Left) && isSame(a.Right, b.Right)
}

