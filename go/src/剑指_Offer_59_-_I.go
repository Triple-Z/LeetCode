func maxSlidingWindow(nums []int, k int) []int {
	if k == 1 {
		return nums
	}
	if len(nums) < 1 {
		return []int{}
	}

	queue := []int{}
	for i := 0; i < k; i++ {
		for len(queue) > 0 && queue[len(queue)-1] < nums[i] {
			queue = queue[:len(queue)-1]
		}
		queue = append(queue, nums[i])
	}

	ans := []int{}
	ans = append(ans, queue[0])

	for i := k; i < len(nums); i++ {
		// remove the last item
		last := nums[i-k]
		if queue[0] == last {
			queue = queue[1:]
		}

		for len(queue) > 0 && queue[len(queue)-1] < nums[i] {
			queue = queue[:len(queue)-1]
		}

		queue = append(queue, nums[i])

		ans = append(ans, queue[0])
	}
	return ans
}