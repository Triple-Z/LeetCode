func maxProfit(prices []int) int {
	n := len(prices)
	if n <= 1 {
		return 0
	}
	minPrice := prices[0]
	// dp[i] = max(dp[i-1], prices[i] - minPrice)
	dp := make([]int, n)
	dp[0] = 0
	for i := 1; i < n; i++ {
		dp[i] = max(dp[i-1], prices[i]-minPrice)
		minPrice = min(minPrice, prices[i])
	}

	return dp[n-1]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}