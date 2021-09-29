func translateNum(num int) int {
	if num < 10 {
		return 1
	} else if num < 26 {
		return 2
	}

	// get the digits
	tmp := num
	digits := []int{}
	for tmp != 0 {
		digit := tmp % 10
		tmp /= 10
		digits = append(digits, digit)
	}

	// reverse digits
	for i, j := 0, len(digits)-1; i < j; i, j = i+1, j-1 {
		digits[i], digits[j] = digits[j], digits[i]
	}

	dp := make([]int, len(digits))
	dp[0] = 1
	if digits[0]*10+digits[1] < 26 {
		dp[1] = 2
	} else {
		dp[1] = 1
	}

	for i := 2; i < len(digits); i++ {
		n := digits[i-1]*10 + digits[i]
		dpIMinusTwo := 0
		if 10 <= n && n < 26 {
			dpIMinusTwo = dp[i-2]
		}

		dp[i] = dp[i-1] + dpIMinusTwo
	}

	return dp[len(digits)-1]
}
