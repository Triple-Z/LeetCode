# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    is_subtree = False

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        self.tranverse(s, t)
        return self.is_subtree
        

    def tranverse(self, root, sub_root):
        
        def equal(root, sub_root):
            if not root and not sub_root:
                return True
            if root and sub_root and root.val == sub_root.val:
                left_rst = equal(root.left, sub_root.left)
                right_rst = equal(root.right, sub_root.right)
                return left_rst and right_rst

        if root:
            
            if equal(root, sub_root):
                self.is_subtree = True

            if root.left:
                self.tranverse(root.left, sub_root)
            if root.right:
                self.tranverse(root.right, sub_root)
