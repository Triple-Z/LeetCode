func myPow(x float64, n int) float64 {
	if n == 0 {
		return 1
	}

	if n < 0 {
		x = 1 / x
		n = -n // n is always positive
	}

	if n%2 == 0 {
		halfPow := myPow(x, n>>1)
		return halfPow * halfPow
	}

	halfPow := myPow(x, (n-1)>>1)
	return halfPow * halfPow * x
}
