func getLeastNumbers(arr []int, k int) []int {
	if k == 0 {
		return []int{}
	}

	sort.Sort(sort.IntSlice(arr))
	return arr[:k]
}