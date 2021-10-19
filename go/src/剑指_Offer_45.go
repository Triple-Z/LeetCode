func minNumber(nums []int) string {
	strs := make([]string, len(nums))
	for i := 0; i < len(nums); i++ {
		strs[i] = strconv.Itoa(nums[i])
	}

	sort.Slice(strs, func(i, j int) bool {
		if strings.Compare(strs[i]+strs[j], strs[j]+strs[i]) == -1 {
			return true
		}
		return false
	})

	builder := strings.Builder{}
	for _, s := range strs {
		builder.WriteString(s)
	}

	return builder.String()
}

