func maxValue(grid [][]int) int {
	m := len(grid)
	if m == 0 {
		return 0
	}
	n := len(grid[0])
	if n == 0 {
		return 0
	}

	var dp [][]int = make([][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([]int, n)
	}

	jSum := 0
	for j := 0; j < n; j++ {
		jSum += grid[0][j]
		dp[0][j] = jSum
	}

	iSum := 0
	for i := 0; i < m; i++ {
		iSum += grid[i][0]
		dp[i][0] = iSum
	}

	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
		}
	}

	return dp[m-1][n-1]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}