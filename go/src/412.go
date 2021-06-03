func fizzBuzz(n int) []string {
	ans := make([]string, n)
	for i := 1; i <= n; i++ {
		str := ""
		if i%3 == 0 {
			str += "Fizz"
		}
		if i%5 == 0 {
			str += "Buzz"
		}
		if str == "" {
			str = strconv.FormatInt(int64(i), 10)
		}
		ans[i-1] = str
	}
	return ans
}