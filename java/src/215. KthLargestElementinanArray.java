class Solution {
    public int findKthLargest(int[] nums, int k) {
        // min heap
        PriorityQueue<Integer> queue = new PriorityQueue();
        for (int num : nums) {
            if (queue.size() == k) {
                if (queue.peek() < num) {
                    // If the current number larger than heap top,
                    // pop the heap top and push this number into 
                    // the min heap.
                    queue.poll();
                    queue.offer(num);
                }
            } else {
                queue.offer(num);
            }
        }
        
        return queue.poll();
    }
}