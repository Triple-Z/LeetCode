/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func kthLargest(root *TreeNode, k int) int {
	if root == nil || k == 0 {
		return -1
	}

	return handler(root, &k).Val
}

func handler(root *TreeNode, k *int) *TreeNode {
	var target *TreeNode

	if root.Right != nil {
		target = handler(root.Right, k)
	}

	if target == nil {
		if *k == 1 {
			return root
		}
		*k--
	}

	if target == nil && root.Left != nil {
		target = handler(root.Left, k)
	}

	return target
}
