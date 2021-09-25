/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func mirrorTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	rootLeft := root.Left
	root.Left = mirrorTree(root.Right)
	root.Right = mirrorTree(rootLeft)

	return root
}