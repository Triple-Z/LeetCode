# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    path = 0
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.traverse(root, sum)
        return self.path

    def traverse(self, root, sum):
        def equal_sum(root, cur_sum, sum):
            if root:
                cur_sum += root.val

                if cur_sum == sum:
                    self.path += 1
                
                equal_sum(root.left, cur_sum, sum)
                equal_sum(root.right, cur_sum, sum)
                
        if root:
            equal_sum(root, 0, sum)
            
            self.traverse(root.left, sum)
            self.traverse(root.right, sum)



        