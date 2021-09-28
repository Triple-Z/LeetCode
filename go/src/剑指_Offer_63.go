func maxProfit(prices []int) int {
	if len(prices) == 0 {
		return 0
	}

	minPrice := prices[0]
	ans := math.MinInt64
	for i := 0; i < len(prices); i++ {
		minPrice = min(minPrice, prices[i])
		ans = max(ans, prices[i]-minPrice)
	}

	return ans
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}