func reverseWords(s string) string {
	i, j := len(s)-1, len(s)-1
	// tranverse backward
	b := strings.Builder{}
	first := true
	for i >= 0 {
		if s[j] == byte(' ') {
			j--
			i = j
			continue
		}
		if s[i] != byte(' ') {
			i--
			continue
		}
		// get a word
		if first {
			first = false
		} else {
			b.WriteString(" ")
		}
		b.WriteString(s[i+1 : j+1])
		j = i
	}

	if i == -1 && i != j {
		if first {
			first = false
		} else {
			b.WriteString(" ")
		}
		b.WriteString(s[i+1 : j+1])
	}

	return b.String()
}