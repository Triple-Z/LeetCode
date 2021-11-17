// translate from Sword to Offer
func dicesProbability(n int) []float64 {
	if n < 1 {
		return []float64{}
	}

	dp := make([][]int, 2)
	for i := 0; i < 2; i++ {
		dp[i] = make([]int, 6*n+1)
	}

	flag := 0

	for i := 1; i <= 6; i++ {
		dp[flag][i] = 1
	}

	for k := 2; k <= n; k++ {
		for i := 0; i < k; i++ {
			// there are k dices, so the min sum will be k.
			dp[1-flag][i] = 0
		}

		for i := k; i <= 6*k; i++ {
			// calc from k to 6*k
			dp[1-flag][i] = 0
			for j := 1; j <= 6 && j < i; j++ {
				dp[1-flag][i] += dp[flag][i-j]
			}
		}
		// switch dice results
		flag = 1 - flag
	}

	total := math.Pow(6, float64(n))
	ans := []float64{}
	for i := n; i <= n*6; i++ {
		ans = append(ans, float64(dp[flag][i])/total)
	}

	return ans
}