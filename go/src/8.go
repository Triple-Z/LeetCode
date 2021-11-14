func myAtoi(str string) int {
	// eat spaces
	str = trim(str)

	if len(str) < 1 {
		return 0
	}

	if str[0] != byte('+') && str[0] != byte('-') && !(str[0] >= byte('0') && str[0] <= byte('9')) {
		// no sign & no digit
		return 0
	}

	sign := 1
	if str[0] == byte('+') {
		str = str[1:]
	} else if str[0] == byte('-') {
		str = str[1:]
		sign = -1
	}

	digits := getDigits(str)

	if len(digits) > 10 {
		if sign > 0 {
			return math.MaxInt32
		} else {
			return math.MinInt32
		}
	}

	ans := 0
	for i := 0; i < len(digits); i++ {
		pos := digits[i] - byte('0')
		ans = ans*10 + int(pos)
	}
	ans = ans * sign

	if ans > math.MaxInt32 {
		return math.MaxInt32
	}
	if ans < math.MinInt32 {
		return math.MinInt32
	}

	return ans
}

func getDigits(str string) string {
	// remove the prefix zeros
	for len(str) > 0 && str[0] == byte('0') {
		str = str[1:]
	}

	start, end := 0, 0
	for ; end < len(str) && str[end] >= byte('0') && str[end] <= byte('9'); end++ {
	}
	return str[start:end]
}

func trim(s string) string {
	for len(s) > 0 && s[0] == byte(' ') {
		s = s[1:]
	}

	return s
}
