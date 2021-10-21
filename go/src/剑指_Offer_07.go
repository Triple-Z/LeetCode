/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) < 1 || len(inorder) < 1 {
		return nil
	}

	rootVal := preorder[0]
	inorderIdx := 0
	for ; inorderIdx < len(inorder); inorderIdx++ {
		if inorder[inorderIdx] == rootVal {
			break
		}
	}

	return &TreeNode{
		Val:   preorder[0],
		Left:  buildTree(preorder[1:1+inorderIdx], inorder[:inorderIdx]),
		Right: buildTree(preorder[1+inorderIdx:], inorder[inorderIdx+1:]),
	}

}