func cuttingRope(n int) int {
	if n == 4 {
		return 4
	} else if n == 3 {
		return 2
	} else if n == 2 {
		return 1
	}

	ans := 1
	for n > 4 {
		n = n - 3
		ans = ans * 3 % 1000000007
	}

	return (ans * n) % 1000000007
}