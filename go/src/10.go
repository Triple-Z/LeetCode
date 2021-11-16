func isMatch(s string, p string) bool {
	if len(s) == 0 && len(p) == 0 {
		return true
	} else if len(s) > 0 && len(p) == 0 {
		return false
	} // p maybe longer than s because of "n*" sequences

	if len(p) > 1 && p[1] == byte('*') {
		if len(s) > 0 && (p[0] == s[0] || p[0] == byte('.')) {
			// "a*" or ".*" state
			// if s is empty, only can ignore current state.
			return isMatch(s[1:], p) || // stay in current state
				isMatch(s[1:], p[2:]) || // go to next state
				isMatch(s, p[2:]) // ignore current state, go to next state
		}
		// no match "a*" in s
		return isMatch(s, p[2:]) // ignore current state, go to next state
	}

	if len(p) > 0 && len(s) > 0 && (p[0] == s[0] || p[0] == byte('.')) {
		// "a" or "." state
		// if s is empty, this pattern won't match.
		return isMatch(s[1:], p[1:]) // go to next state
	}

	return false
}