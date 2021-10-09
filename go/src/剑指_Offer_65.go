func add(a int, b int) int {
	var sum, ci int
	for b != 0 {
		sum = a ^ b
		ci = a & b << 1
		a, b = sum, ci
	}
	return a
}