func minArray(numbers []int) int {
	min := math.MaxInt64
	for i := len(numbers) - 1; i >= 0; i-- {
		if numbers[i] > min {
			return min
		}
		min = Min(min, numbers[i])
	}
	return min
}

func Min(a int, b int) int {
	if a < b {
		return a
	}

	return b
}