class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = list()

        def recursive(s = '', left = 0, right = 0):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if left < n:
                recursive(s + '(', left+1, right)
            if left > right:
                recursive(s + ')', left, right+1)
        
        recursive()

        return ans

