class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> numCnt = new HashMap<>();
        
        for (int num : nums) {
            numCnt.put(num, numCnt.getOrDefault(num, 0) + 1);
        }
        
        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(numCnt.entrySet());
        list.sort(Collections.reverseOrder(Map.Entry.comparingByValue()));

        int[] ans = new int[k];
        for (int i = 0; i < k; i++) {
            ans[i] = list.get(i).getKey();
        }

        return ans;
    }
}