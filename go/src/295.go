type MinHeap []int

func (h MinHeap) Len() int {
	return len(h)
}

func (h MinHeap) Less(i, j int) bool {
	return h[i] < h[j]
}

func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	*h = old[:n-1]
	return old[n-1]
}

type MaxHeap []int

func (h MaxHeap) Len() int {
	return len(h)
}

func (h MaxHeap) Less(i, j int) bool {
	return h[i] > h[j]
}

func (h MaxHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	*h = old[:n-1]
	return old[n-1]
}

type MedianFinder struct {
	minHeap MinHeap
	maxHeap MaxHeap
}

func Constructor() MedianFinder {
	return MedianFinder{}
}

func (this *MedianFinder) AddNum(num int) {
	maxHeap, minHeap := &this.maxHeap, &this.minHeap
	if maxHeap.Len() == 0 || num <= (*maxHeap)[0] {
		// add num to maxHeap
		heap.Push(maxHeap, num)
		if maxHeap.Len() > minHeap.Len()+1 {
			// move an element from maxHeap to minHeap
			heap.Push(minHeap, heap.Pop(maxHeap).(int))
		}
	} else {
		// add num to minHeap
		heap.Push(minHeap, num)
		if minHeap.Len() > maxHeap.Len() {
			// move an element from minHeap to maxHeap
			heap.Push(maxHeap, heap.Pop(minHeap).(int))
		}
	}
}

func (this *MedianFinder) FindMedian() float64 {
	if this.maxHeap.Len() == this.minHeap.Len() {
		return float64(this.maxHeap[0]+this.minHeap[0]) / 2.0
	}
	return float64(this.maxHeap[0])
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */