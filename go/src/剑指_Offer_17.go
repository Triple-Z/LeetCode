func printNumbers(n int) []int {
	upper := pow(10, n)
	ans := make([]int, upper-1)

	for i := 0; i < len(ans); i++ {
		ans[i] = i + 1
	}

	return ans
}

func pow(base, n int) int {
	ans := 1
	for i := 0; i < n; i++ {
		ans *= base
	}
	return ans
}