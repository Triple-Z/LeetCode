class MinStack {

    Deque<Integer> stack;
    int minValue;

    /** initialize your data structure here. */
    public MinStack() {
        stack = new LinkedList<Integer>();
        minValue = Integer.MAX_VALUE;
    }
    
    public void push(int x) {
        stack.push(x);
        minValue = Math.min(minValue, x);
    }
    
    public void pop() {
        Integer p = stack.pop();
        if (p != null && p.equals(minValue)) {
            // re-find min value
            minValue = Integer.MAX_VALUE;
            for (int i : stack) {
                minValue = Math.min(minValue, i);
            }
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minValue;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */