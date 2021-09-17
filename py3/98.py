# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def _isValidBST(root: TreeNode, upper: float, lower: float) -> bool:
            if not root:
                return True

            if root.val >= upper or root.val <= lower:
                return False
            
            if not _isValidBST(root.left, root.val, lower):
                return False
            if not _isValidBST(root.right, upper, root.val):
                return False
            
            return True
        
        return _isValidBST(root, float('inf'), float('-inf'))