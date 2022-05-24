/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumNumbers(root *TreeNode) int {
	if root == nil {
		return 0
	}

	nums := getNumbers(root, 0)

	sum := 0
	for _, v := range nums {
		sum += v
	}

	return sum
}

func getNumbers(root *TreeNode, curNum int) []int {
	if root == nil {
		return []int{}
	}

	curNum = curNum*10 + root.Val
	if root.Left == nil && root.Right == nil {
		return []int{curNum}
	}

	leftNums := getNumbers(root.Left, curNum)
	nums := append(leftNums, getNumbers(root.Right, curNum)...)

	return nums
}
