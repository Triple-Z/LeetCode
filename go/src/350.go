func intersect(nums1 []int, nums2 []int) []int {
	sort.Ints(nums1)
	sort.Ints(nums2)

	x := 0
	y := 0
	res := []int{}

	for x < len(nums1) && y < len(nums2) {
		if nums1[x] == nums2[y] {
			res = append(res, nums1[x])
			x++
			y++
		} else if nums1[x] > nums2[y] {
			y++
		} else {
			x++
		}
	}

	return res
}