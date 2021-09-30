func exchange(nums []int) []int {
	p, q := 0, len(nums)-1
	for p < q {
		// odds in front, evens in end
		if nums[p]%2 == 0 && nums[q]%2 == 1 {
			nums[p], nums[q] = nums[q], nums[p]
		}
		if nums[p]%2 != 0 {
			p++
		}
		if nums[q]%2 != 1 {
			q--
		}
	}

	return nums
}