func maxSubArray(nums []int) int {
	dp := make([]int, len(nums))
	ans := nums[0]

	dp[0] = nums[0]
	for i := 1; i < len(nums); i++ {
		dp[i] = max(nums[i], nums[i]+dp[i-1])
		ans = max(ans, dp[i])
	}

	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}