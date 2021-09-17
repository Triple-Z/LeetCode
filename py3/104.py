# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def _maxDepth(root: TreeNode, depth: int) -> int:
            if root is None:
                return depth
            left_depth, right_depth = depth, depth
            if root.left:
                left_depth = _maxDepth(root.left, depth+1)
            if root.right:
                right_depth = _maxDepth(root.right, depth+1)
            return max(left_depth, right_depth)
        
        return _maxDepth(root, 1)