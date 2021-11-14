func validateStackSequences(pushed []int, popped []int) bool {
	push, pop := 0, 0
	stack := []int{}
	for ; push < len(pushed); push++ {
		stack = append(stack, pushed[push])
		for len(stack) > 0 && pop < len(popped) && stack[len(stack)-1] == popped[pop] {
			stack = stack[:len(stack)-1]
			pop++
		}
	}

	if pop == len(popped) {
		return true
	}
	return false
}