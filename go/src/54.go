func spiralOrder(matrix [][]int) []int {
	m := len(matrix)
	if m == 0 {
		return []int{}
	}
	n := len(matrix[0])
	if n == 0 {
		return []int{}
	}

	layer := 0
	ans := []int{}
	total := m * n
	for len(ans) < total {
		// left
		for col := layer; col < n-layer; col++ {
			ans = append(ans, matrix[layer][col])
		}
		if len(ans) == total {
			break
		}
		// down
		for row := layer + 1; row < m-layer; row++ {
			ans = append(ans, matrix[row][n-layer-1])
		}
		if len(ans) == total {
			break
		}
		// left
		for col := n - layer - 2; col >= layer; col-- {
			ans = append(ans, matrix[m-layer-1][col])
		}
		if len(ans) == total {
			break
		}
		// up
		for row := m - layer - 2; row > layer; row-- {
			ans = append(ans, matrix[row][layer])
		}
		layer++
	}

	return ans

}