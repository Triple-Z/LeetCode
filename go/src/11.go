func maxArea(height []int) int {
	i := 0
	j := len(height) - 1

	max := 0

	for i < j {
		curVol := min(height[i], height[j]) * (j - i)
		if max < curVol {
			max = curVol
		}
		if height[i] <= height[j] {
			i++
		} else {
			j--
		}
	}

	return max
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}