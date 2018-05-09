class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        palin_start, palin_end, palin_max_len = 0, 0, 0

        for i in range(len(s)):
            dp[i][i] = True

        for j in range(len(s)):
            for i in range(j):

                if s[i] == s[j]:
                    # this string is palindrome
                    if i < j and i+1 < j-1:
                        dp[i][j] = dp[i+1][j-1]
                    else:
                        dp[i][j] = True
                    
                    if j - i + 1 > palin_max_len and dp[i][j]:
                        palin_max_len = j - i + 1
                        palin_start = i
                        palin_end = j
                else:
                    dp[i][j] = False
        # print(dp)
        # print(palin_start, palin_end)
        return s[palin_start:palin_end+1]


# solute = Solution()
# print(solute.longestPalindrome("babad"))
# print(solute.longestPalindrome("abcda"))
# print(solute.longestPalindrome("cbbd"))
# print(solute.longestPalindrome("aaaa"))
