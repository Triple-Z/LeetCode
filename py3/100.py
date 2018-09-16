# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False
        else:
            if p.val != q.val:
                return False
            else:
#                 p.val == q.val, continue...
                left, right = False, False
                left = self.isSameTree(p.left, q.left)
                right = self.isSameTree(p.right, q.right)
                
                return left and right
                