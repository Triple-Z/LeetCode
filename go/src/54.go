func spiralOrder(matrix [][]int) []int {
	n := len(matrix)
	if n == 0 {
		return []int{}
	}
	m := len(matrix[0])

	l, u := 0, 0
	r, b := m-1, n-1
	i, j := 0, 0 // entry from (0, 0)

	const (
		LEFT_RIGHT = iota
		UPPER_BOTTOM
		RIGHT_LEFT
		BOTTOM_UPPER
	)

	curDirection := LEFT_RIGHT

	ans := make([]int, n*m)
	for k := 0; k < n*m && l <= r && u <= b; k++ {
		if i == u && j == r && curDirection == LEFT_RIGHT {
			// hit upper-right
			u++
			curDirection = UPPER_BOTTOM
		} else if i == b && j == r && curDirection == UPPER_BOTTOM {
			// hit bottom-right
			r--
			curDirection = RIGHT_LEFT
		} else if i == b && j == l && curDirection == RIGHT_LEFT {
			// hit bottom-left
			b--
			curDirection = BOTTOM_UPPER
		} else if i == u && j == l && curDirection == BOTTOM_UPPER {
			// hit upper-left
			l++
			curDirection = LEFT_RIGHT
		}

		ans[k] = matrix[i][j]

		if curDirection == UPPER_BOTTOM {
			i++
		} else if curDirection == RIGHT_LEFT {
			j--
		} else if curDirection == BOTTOM_UPPER {
			i--
		} else if curDirection == LEFT_RIGHT {
			j++
		}
	}

	return ans
}