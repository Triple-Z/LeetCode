class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0 for _ in range(0, num+1)]
        dp[0], offset = 0, 1
        for i in range(1, num+1):
            if offset * 2 == i:
                offset = i
            dp[i] = dp[i - offset] + 1
        
        return dp

