func majorityElement(nums []int) int {
	if len(nums) < 1 {
		return -1
	}

	ans := nums[0]
	times := 1
	for i := 1; i < len(nums); i++ {
		if times == 0 {
			ans = nums[i]
			times = 1
		} else if ans == nums[i] {
			times++
		} else {
			times--
		}
	}

	return ans
}