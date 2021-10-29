func lengthOfLongestSubstring(s string) int {
	if s == "" {
		return 0
	}

	cMap := make(map[byte]bool)
	i, j := 0, 1
	cMap[s[i]] = true
	maxChars := 1
	for i <= j && j < len(s) {
		if _, ok := cMap[s[j]]; ok {
			// last string: [i, j)
			maxChars = max(maxChars, j-i)
			for s[i] != s[j] {
				delete(cMap, s[i])
				i++
			}
			delete(cMap, s[i])
			i++
			continue
		}
		cMap[s[j]] = true
		j++
	}
	if j == len(s) {
		maxChars = max(maxChars, j-i)
	}

	return maxChars
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}