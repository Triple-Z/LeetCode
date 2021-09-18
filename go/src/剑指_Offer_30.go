type MinStack struct {
	minStack []int
	s        []int
}

/** initialize your data structure here. */
func Constructor() MinStack {
	return MinStack{
		minStack: []int{},
		s:        []int{},
	}
}

func (this *MinStack) Push(x int) {
	this.s = append(this.s, x)

	if len(this.minStack) == 0 || x < this.minStack[len(this.minStack)-1] {
		this.minStack = append(this.minStack, x)
		return
	}

	this.minStack = append(this.minStack, this.minStack[len(this.minStack)-1])
}

func (this *MinStack) Pop() {
	this.s = this.s[:len(this.s)-1]
	this.minStack = this.minStack[:len(this.minStack)-1]
}

func (this *MinStack) Top() int {
	return this.s[len(this.s)-1]
}

func (this *MinStack) Min() int {
	return this.minStack[len(this.minStack)-1]
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Min();
 */
