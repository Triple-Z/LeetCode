func twoSum(nums []int, target int) []int {
	p, q := 0, len(nums)-1
	for p < q {
		sum := nums[p] + nums[q]
		if sum > target {
			q--
		} else if nums[p]+nums[q] == target {
			return []int{nums[p], nums[q]}
		} else {
			p++
		}
	}

	return []int{}
}