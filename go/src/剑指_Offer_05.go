func replaceSpace(s string) string {
	b := strings.Builder{}
	for _, c := range s {
		if c == ' ' {
			b.WriteString("%20")
		} else {
			b.WriteRune(c)
		}
	}

	return b.String()
}