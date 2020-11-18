class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> numCnt = new HashMap<>();

        for (int num : nums) {
            numCnt.put(num, numCnt.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<int[]> queue = new PriorityQueue<>(new Comparator<int[]>() {
            public int compare(int[] o1, int[] o2) {
                // if o1[1] < o2[1], and the o1 object should be ahead of the o2,
                // then it should return the `o1[1] - o2[1]`.
                //
                // o1[1] < o2[1] ==> o1[1] - o2[1] < 0

                return o1[1] - o2[1];
            }
        });

        // min heap
        for (Map.Entry<Integer, Integer> entry : numCnt.entrySet()) {
            int num = entry.getKey(), count = entry.getValue();
            if (queue.size() == k) {
                if (queue.peek()[1] < count) {
                    queue.poll();
                    queue.offer(new int[] { num, count });
                }
            } else {
                queue.offer(new int[] { num, count });
            }
        }

        int[] ans = new int[k];
        for (int i = k - 1; i >= 0; i--) {
            // if in order
            ans[i] = queue.poll()[0];
        }

        return ans;
    }
}