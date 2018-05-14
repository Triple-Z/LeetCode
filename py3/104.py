# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    max_depth = 0

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.preorder_traverse(root, 0)
        return self.max_depth

    def preorder_traverse(self, root, cur_depth):
        if root:
            cur_depth += 1
            if self.max_depth < cur_depth:
                self.max_depth = cur_depth
            if root.right is not None or root.left is not None:

                self.preorder_traverse(root.left, cur_depth)
                self.preorder_traverse(root.right, cur_depth)

