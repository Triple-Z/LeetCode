class Solution {
    public int uniquePaths(int m, int n) {
        if (m <= 1 || n <= 1) return 1;
        
        // dp init
        int[][] dp = new int[n][m];
        dp[0][0] = 0;
        dp[0][1] = 1;
        dp[1][0] = 1;

        // dp[i, j] = dp[i-1, j] + dp[i, j-1]
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // skip the init values
                // you can use an extra row & column to optimize it.
                if (i == 0 && j == 0 || i == 0 && j == 1 || i == 1 && j == 0) continue;

                int upVal = i-1 >= 0 ? dp[i-1][j] : 0;
                int leftVal = j-1 >= 0 ? dp[i][j-1] : 0;
                dp[i][j] = upVal + leftVal;
            }
        }

        return dp[n-1][m-1];
    }
}