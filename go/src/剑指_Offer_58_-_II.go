func reverseLeftWords(s string, n int) string {
	b := strings.Builder{}
	for i := n; i < len(s); i++ {
		b.WriteByte(s[i])
	}
	for i := 0; i < n; i++ {
		b.WriteByte(s[i])
	}

	return b.String()
}