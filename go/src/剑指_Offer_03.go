func findRepeatNumber(nums []int) int {
	nMap := make(map[int]int)
	for _, n := range nums {
		if _, ok := nMap[n]; ok {
			return n
		}
		nMap[n] = 1
	}

	return -1
}