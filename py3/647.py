class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        palin_num = 0
        dp = [[ False for _ in range(len(s))] for _ in range(len(s))]

        for x in range(len(s)):
            dp[x][x] = True
            palin_num += 1
        
        for j in range(0, len(s)):
            for i in range(0, j):
                if s[i] == s[j]:
                    if i < j and i + 1 < j - 1:
                        dp[i][j] = dp[i+1][j-1]
                        if dp[i][j]:
                            palin_num += 1
                    else:
                        # i + 1 = j
                        dp[i][j] = True
                        palin_num += 1
        
        return palin_num