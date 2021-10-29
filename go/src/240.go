func findNumberIn2DArray(matrix [][]int, target int) bool {
	if len(matrix) == 0 {
		return false
	}

	n := len(matrix)
	m := len(matrix[0])

	// [i][j] is the top-right corner element
	i := 0
	j := m - 1

	for i < n && j >= 0 {
		if matrix[i][j] == target {
			return true
		}

		if matrix[i][j] > target {
			j--
		} else {
			i++
		}
	}

	return false
}