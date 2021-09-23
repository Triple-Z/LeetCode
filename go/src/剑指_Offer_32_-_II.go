/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}

	q := list.New()

	q.PushBack(root)

	ans := [][]int{}
	for q.Len() > 0 {
		level := []int{}
		curLen := q.Len()
		for i := 0; i < curLen; i++ {
			// pop out current level nodes
			node := q.Remove(q.Front()).(*TreeNode)
			level = append(level, node.Val)
			if node.Left != nil {
				q.PushBack(node.Left)
			}
			if node.Right != nil {
				q.PushBack(node.Right)
			}
		}
		ans = append(ans, level)
	}

	return ans
}