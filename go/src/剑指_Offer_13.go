func movingCount(m int, n int, k int) int {
	queue := list.New()
	directions := [][]int{
		{0, 1},
		{1, 0},
	}
	visited := make([][]bool, m)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}

	queue.PushBack([]int{0, 0})
	visited[0][0] = true

	ans := 0
	for queue.Len() > 0 {
		curPos := queue.Remove(queue.Front()).([]int)
		ans++
		for i := 0; i < 2; i++ {
			newX := curPos[0] + directions[i][0]
			newY := curPos[1] + directions[i][1]
			xySum := newX/10 + newX%10 + newY/10 + newY%10
			if newX >= 0 && newX < m && newY >= 0 && newY < n && !visited[newX][newY] && xySum <= k {
				queue.PushBack([]int{newX, newY})
				visited[newX][newY] = true
			}
		}
	}

	return ans
}