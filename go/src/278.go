func firstBadVersion(n int) int {
	return recursive(1, n)
}

func recursive(first, last int) int {
	if first == last {
		return first
	} else if first > last {
		return -1
	}

	mid := first + (last-first)>>1
	if isBadVersion(mid) {
		return recursive(first, mid)
	} else {
		return recursive(mid+1, last)
	}
}