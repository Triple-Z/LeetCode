func sortArray(nums []int) []int {
	// merge sort
	n := len(nums)

	if n < 1 {
		return []int{}
	}

	if n == 1 {
		return nums
	}

	mid := n / 2
	leftOri, rightOri := make([]int, mid), make([]int, n-mid)
	copy(leftOri, nums[:mid])
	copy(rightOri, nums[mid:])
	left := sortArray(leftOri)
	right := sortArray(rightOri)

	p1, p2 := 0, 0

	i := 0
	for p1 < len(left) && p2 < len(right) {
		if left[p1] < right[p2] {
			nums[i] = left[p1]
			p1++
		} else {
			nums[i] = right[p2]
			p2++
		}
		i++
	}

	for p1 < len(left) {
		nums[i] = left[p1]
		p1++
		i++
	}

	for p2 < len(right) {
		nums[i] = right[p2]
		p2++
		i++
	}

	return nums
}