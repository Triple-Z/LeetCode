func firstUniqChar(s string) int {
	cMap := make(map[rune]int, 0)
	for _, c := range s {
		cMap[c]++
	}

	for i, c := range s {
		if count, _ := cMap[c]; count == 1 {
			return i
		}
	}

	return -1
}