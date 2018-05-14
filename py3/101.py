# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def is_mirror(t1, t2):
            if t1 is None and t2 is None:
                return True
            elif t1 is None or t2 is None:
                return False
            elif t1.val == t2.val:
                left_right = is_mirror(t1.left, t2.right)
                right_left = is_mirror(t1.right, t2.left)
                if left_right and right_left:
                    # print("TRUE")
                    return True
                    
                else: 
                    return False
        
        return is_mirror(root, root)
