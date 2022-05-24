/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

var sums []int

func findFrequentTreeSum(root *TreeNode) []int {
	sums = []int{}
	getAllSums(root)

	sumMap := make(map[int]int)
	maxFrequency := 0

	for _, sum := range sums {
		if _, ok := sumMap[sum]; !ok {
			sumMap[sum] = 0
		}
		sumMap[sum]++
		if sumMap[sum] > maxFrequency {
			maxFrequency = sumMap[sum]
		}
	}

	ans := []int{}
	for k, v := range sumMap {
		if v == maxFrequency {
			ans = append(ans, k)
		}
	}

	return ans
}

func getAllSums(root *TreeNode) int {
	if root == nil {
		return 0
	}

	leftSum := getAllSums(root.Left)
	rightSum := getAllSums(root.Right)

	curSum := leftSum + rightSum + root.Val
	sums = append(sums, curSum)
	return curSum
}
 