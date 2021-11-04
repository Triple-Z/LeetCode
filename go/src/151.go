func reverseWords(s string) string {
	words := strings.Split(s, " ")
	ans := strings.Builder{}
	first := true
	for i := len(words) - 1; i >= 0; i-- {
		if words[i] != "" {
			if !first {
				ans.WriteString(" ")
			} else {
				first = false
			}
			ans.WriteString(strings.Trim(words[i], " "))
		}
	}

	return ans.String()
}