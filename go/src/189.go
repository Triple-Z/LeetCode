func reverse(nums []int) {
	length := len(nums)
	for i := 0; i < length/2; i++ {
		nums[i], nums[length-i-1] = nums[length-i-1], nums[i]
	}
}

func rotate(nums []int, k int) {
	if len(nums) == 0 {
		return
	}

	k %= len(nums)
	reverse(nums[:])
	reverse(nums[:k])
	reverse(nums[k:])
}