func nthUglyNumber(n int) int {
	dp := make([]int, n)

	dp[0] = 1
	t2, t3, t5 := 0, 0, 0
	for i := 1; i < n; i++ {
		min := min3(dp[t2]*2, dp[t3]*3, dp[t5]*5)
		dp[i] = min

		for t2 < i && dp[t2]*2 <= min {
			t2++
		}
		for t3 < i && dp[t3]*3 <= min {
			t3++
		}
		for t5 < i && dp[t5]*5 <= min {
			t5++
		}

	}

	return dp[n-1]
}

func min3(a, b, c int) int {
	var min int = a
	if b < a {
		min = b
	}

	if c < min {
		min = c
	}

	return min
}