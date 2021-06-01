func removeDuplicates(nums []int) int {
	if len(nums) < 1 {
		return 0
	}
	if len(nums) == 1 {
		return 1
	}

	length := 1
	for i := 1; i < len(nums); i++ {
		if nums[i] != nums[i-1] {
			nums[length] = nums[i]
			length++
		}
	}

	return length
}