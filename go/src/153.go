func findMin(nums []int) int {
	n := len(nums)

	if n == 1 {
		return nums[0]
	}

	l, r := 0, n-1
	for l < r {
		mid := l + (r-l)>>1
		if nums[mid] > nums[r] {
			l = mid + 1
		} else {
			r = mid
		}
	}

	return nums[l]
}