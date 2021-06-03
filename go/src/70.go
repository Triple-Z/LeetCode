func climbStairs(n int) int {
	dp := make([]int, 2)
	dp[0] = 1
	dp[1] = 2
	for i := 2; i < n; i++ {
		dp = append(dp, dp[i-1]+dp[i-2])
	}
	return dp[n-1]
}