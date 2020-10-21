class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        if (n < 2) return s;

        String ans = "";
        boolean[][] dp = new boolean[n][n];

        for (int i = n-1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (s.charAt(i) != s.charAt(j)) dp[i][j] = false;
                else {
                    // (j-1) - (i+1) + 1 < 2
                    if (j - i < 3) {
                        // dp[i+1][j-1] is a single character.
                        // and charAt(i) == charAt(j)
                        dp[i][j] = true;
                    } else {
                        dp[i][j] = dp[i+1][j-1];
                    }
                }

                if (dp[i][j] && j-i+1 > ans.length()) {
                    ans = s.substring(i, j+1);
                }
            }
        }

        return ans;
    }
}