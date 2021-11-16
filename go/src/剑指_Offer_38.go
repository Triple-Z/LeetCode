func permutation(s string) []string {
	ansMap := make(map[string]bool) // for remove duplication

	if len(s) == 1 {
		return []string{s}
	}

	var permutationCore func(string, string)
	permutationCore = func(cur string, remain string) {
		if len(remain) == 0 {
			ansMap[cur] = true
		}

		for i := 0; i < len(remain); i++ {
			// don't change cur/remain for backtrack
			newCur := cur + string(remain[i])
			newRemain := remain[:i] + remain[i+1:]

			permutationCore(newCur, newRemain)
		}
	}

	permutationCore("", s)

	ans := []string{}
	for permuteStr, _ := range ansMap {
		ans = append(ans, permuteStr)
	}

	return ans
}

