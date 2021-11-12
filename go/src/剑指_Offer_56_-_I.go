func singleNumbers(nums []int) []int {
	t := 0
	for i := 0; i < len(nums); i++ {
		t ^= nums[i]
	}

	mask := 1
	for (mask & t) == 0 {
		mask <<= 1
	}

	num1, num2 := 0, 0
	for i := 0; i < len(nums); i++ {
		if (nums[i] & mask) != 0 {
			// the target position of num[i] is 1
			num1 ^= nums[i]
		} else {
			// the target position of num[i] is 0
			num2 ^= nums[i]
		}
	}

	return []int{num1, num2}
}