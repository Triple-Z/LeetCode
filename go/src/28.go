func strStr(haystack string, needle string) int {
	if len(needle) == 0 {
		return 0
	}

	for i := 0; i <= len(haystack)-len(needle); i++ {
		if haystack[i] == needle[0] {
			match := findMatch([]byte(haystack[i:]), needle)
			if match {
				return i
			}
		}
	}

	return -1
}

func findMatch(str []byte, target string) bool {
	i := 0
	for j := 0; j < len(target); j++ {
		if i >= len(str) {
			return false
		}
		if str[i] != target[j] {
			return false
		}
		i++
	}

	return true
}