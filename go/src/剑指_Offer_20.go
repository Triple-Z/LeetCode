func isNumber(s string) bool {
	s = isSpace(s)

	if strings.Contains(s, ".") {
		s = isFloat(s)
	} else {
		s = isInteger(s)
	}

	if len(s) > 1 && (s[0] == byte('e') || s[0] == byte('E')) {
		// has 'e' or 'E'
		s = s[1:]
		s = isInteger(s)
	}

	s = isSpace(s)

	if len(s) == 0 {
		return true
	}

	return false
}

func isSpace(s string) string {
	for len(s) > 0 && s[0] == byte(' ') {
		s = s[1:]
	}
	return s
}

func isFloat(s string) string {
	s = isSign(s)
	if len(s) < 1 {
		return "ERROR"
	}
	if s[0] == byte('.') {
		s = s[1:]
		s = isDigits(s)
		return s
	}

	s = isDigits(s)
	if s[0] != byte('.') {
		return "ERROR"
	}
	s = s[1:] // eat the dot
	if len(s) > 0 && (s[0] >= byte('0') && s[0] <= byte('9')) {
		s = isDigits(s)
	}

	return s
}

func isInteger(s string) string {
	s = isSign(s)
	s = isDigits(s)

	return s
}

func isDigits(s string) string {
	// at least one digit
	i := 0
	for len(s) > 0 && (s[0] >= byte('0') && s[0] <= byte('9')) {
		s = s[1:]
		i++
	}

	if i < 1 {
		return "ERROR"
	}
	return s
}

func isSign(s string) string {
	if len(s) > 0 && (s[0] == byte('+') || s[0] == byte('-')) {
		s = s[1:]
	}
	return s
}