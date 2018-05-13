# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        p1, p2 = t1, t2

        if t2 is None:
            return t1

        def merge(p1, p2):
            """
            Merge two tree to tree 2 and return.
            """
            if p1 is None:
                return None
            elif p1 is not None and p2 is not None:
                p2.val += p1.val
                

            if p1.left is not None and p2.left is None:
                p2.left = TreeNode(0)
            
            merge(p1.left, p2.left)

            if p1.right is not None and p2.right is None:
                p2.right = TreeNode(0)
            merge(p1.right, p2.right)

        merge(p1, p2)

        return t2
