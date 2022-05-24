/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func hasPathSum(root *TreeNode, targetSum int) bool {
	return handler(root, targetSum, 0)
}

func handler(root *TreeNode, targetSum, currentSum int) bool {
	if root == nil {
		return false
	}

	currentSum += root.Val
	if root.Left == nil && root.Right == nil && currentSum == targetSum {
		return true
	}

	return handler(root.Left, targetSum, currentSum) ||
		handler(root.Right, targetSum, currentSum)
}
