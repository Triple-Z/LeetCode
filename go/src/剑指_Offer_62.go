func lastRemaining(n int, m int) int {
	ans := 0
	for i := 2; i <= n; i++ {
		ans = (ans + m) % i
	}

	return ans
}