# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.rst = list()

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Recursive method
        self.inorder_traverse(root)
        return self.rst

        # TODO: Iteration method
        

    def inorder_traverse(self, root):
        if root:
            self.inorder_traverse(root.left)
            if root.val is not None:
                self.rst.append(root.val)
            self.inorder_traverse(root.right)
        

                
