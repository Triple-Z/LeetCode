func cuttingRope(n int) int {
	if n == 2 {
		return 1
	} else if n == 3 {
		return 2
	}

	rope3 := n / 3
	if n%3 == 1 {
		rope3--
	}

	rope2 := (n - 3*rope3) / 2

	return int(math.Pow(3.0, float64(rope3))) * int(math.Pow(2.0, float64(rope2)))
}