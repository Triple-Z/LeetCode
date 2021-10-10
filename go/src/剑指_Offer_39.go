func majorityElement(nums []int) int {
	sort.Sort(sort.IntSlice(nums))
	return nums[len(nums)/2]
}