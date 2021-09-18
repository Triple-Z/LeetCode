type CQueue struct {
	s1 []int
	s2 []int
}

func Constructor() CQueue {
	return CQueue{
		s1: []int{},
		s2: []int{},
	}
}

func (this *CQueue) AppendTail(value int) {
	// add value to stack 1
	this.s1 = append(this.s1, value)
}

func (this *CQueue) DeleteHead() int {

	if len(this.s2) == 0 {
		// move all elements from stack 1 to stack 2
		for len(this.s1) > 0 {
			m := this.s1[len(this.s1)-1]
			this.s2 = append(this.s2, m)
			this.s1 = this.s1[:len(this.s1)-1]
		}
		// clear stack 1
		this.s1 = []int{}
	}

	if len(this.s2) > 0 {
		// remove the top element
		head := this.s2[len(this.s2)-1]
		this.s2 = this.s2[:len(this.s2)-1]
		return head
	}

	return -1
}

/**
 * Your CQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AppendTail(value);
 * param_2 := obj.DeleteHead();
 */
