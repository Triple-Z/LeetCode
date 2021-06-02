func rotate(nums []int, k int) {
	n := len(nums)
	if n == 1 {
		return
	}
	res := make([]int, n)
	for i, num := range nums {
		target := (i + k) % n
		res[target] = num
	}

	for i, _ := range nums {
		nums[i] = res[i]
	}
}