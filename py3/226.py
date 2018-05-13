# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
	def invertTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		if root is None:
			return None
		
		right = self.invertTree(root.right)
		left = self.invertTree(root.left)
		root.right = left
		root.left = right

		return root
