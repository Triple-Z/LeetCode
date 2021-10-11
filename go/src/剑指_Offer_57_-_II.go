func findContinuousSequence(target int) [][]int {
	i, j := 1, 2
	ans := [][]int{}
	for i < j {
		sum := (j - i + 1) * (i + j) / 2
		if sum == target {
			li := []int{}
			for k := i; k <= j; k++ {
				li = append(li, k)
			}
			ans = append(ans, li)
			i++
		} else if sum > target {
			i++
		} else {
			j++
		}
	}

	return ans
}