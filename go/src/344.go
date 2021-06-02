func reverseString(s []byte) {
	n := len(s)
	for i := 0; i < n/2; i++ {
		swap(s, i, n-1-i)
	}
}

func swap(s []byte, i, j int) {
	tmp := s[i]
	s[i] = s[j]
	s[j] = tmp
}