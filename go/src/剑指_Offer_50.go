func firstUniqChar(s string) byte {
	cMap := make(map[byte]int)
	order := []byte{}

	for i := 0; i < len(s); i++ {
		if last, ok := cMap[s[i]]; ok {
			cMap[s[i]] = last + 1
		} else {
			order = append(order, s[i])
			cMap[s[i]] = 1
		}
	}

	for _, c := range order {
		if cMap[c] == 1 {
			return c
		}
	}

	return byte(' ')
}