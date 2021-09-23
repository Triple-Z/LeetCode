func search(nums []int, target int) int {
	// iteration
	sum := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] == target {
			sum++
		} else if nums[i] > target {
			break
		}
	}
	return sum
}