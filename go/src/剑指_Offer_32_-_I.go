/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	queue := list.New()
	queue.PushBack(root) // push
	ans := []int{}

	for queue.Len() > 0 {
		node := queue.Remove(queue.Front()).(*TreeNode) // pop
		ans = append(ans, node.Val)
		if node.Left != nil {
			queue.PushBack(node.Left) // push
		}
		if node.Right != nil {
			queue.PushBack(node.Right) //push
		}
	}

	return ans
}