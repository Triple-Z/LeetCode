func isStraight(nums []int) bool {
	nMap := make(map[int]bool)
	nMin := 14
	nMax := -1

	for i := 0; i < 5; i++ {
		if nums[i] == 0 {
			continue
		}
		if _, ok := nMap[nums[i]]; ok {
			// duplicate
			return false
		}
		nMap[nums[i]] = true
		nMax = max(nMax, nums[i])
		nMin = min(nMin, nums[i])
	}

	return nMax-nMin < 5
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}