# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    max_d = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_d = 1
        self.traverse(root)
        return self.max_d

    def traverse(self, root):
        if root:
            L = self.traverse(root.left)
            R = self.traverse(root.right)
            self.max_d = max(self.max_d, L+R)
            return max(L, R) + 1
        return 0
