func singleNumber(nums []int) int {
	bitSum := make([]int, 32)

	for i := 0; i < len(nums); i++ {
		mask := 1
		for j := 0; j < 32; j++ {
			if nums[i]&mask != 0 {
				// nums[i](j) bit is 1
				bitSum[j] += 1
			}

			mask = mask << 1
		}
	}

	mask := 1
	ans := 0
	for i := 0; i < 32; i++ {
		if bitSum[i]%3 == 0 {
			// ans(i) bit is 0
			ans = ans & (^mask)
		} else {
			// ans(i) bit is 1
			ans = ans | mask
		}
		mask = mask << 1
	}

	return ans
}