/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pathSum(root *TreeNode, target int) [][]int {
	if root == nil {
		return [][]int{}
	}

	return pathSumCore(root, target, 0, [][]int{}, []int{})
}

func pathSumCore(root *TreeNode, target, curSum int, ans [][]int, curNodes []int) [][]int {
	if root == nil {
		return ans
	}

	curSum += root.Val
	curNodes = append(curNodes, root.Val)

	if curSum == target && root.Left == nil && root.Right == nil {
		nodes := make([]int, len(curNodes))
		copy(nodes, curNodes)
		ans = append(ans, nodes)
		curNodes = curNodes[:len(curNodes)-1]
		return ans
	}

	if root.Left != nil {
		ans = pathSumCore(root.Left, target, curSum, ans, curNodes)
	}

	if root.Right != nil {
		ans = pathSumCore(root.Right, target, curSum, ans, curNodes)
	}

	return ans
}