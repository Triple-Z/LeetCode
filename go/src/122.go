func maxProfit(prices []int) int {
	n := len(prices)
	if n == 1 {
		return 0
	}

	res := 0
	for i := 1; i < n; i++ {
		if prices[i-1] < prices[i] {
			res += (prices[i] - prices[i-1])
		}
	}
	return res
}