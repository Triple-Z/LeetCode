class Solution {
    public int majorityElement(int[] nums) {
        int midBound = nums.length / 2;
        Map<Integer, Integer> cntMap = new HashMap<>();

        for (int num : nums) {
            cntMap.put(num, cntMap.getOrDefault(num, 0) + 1);
            if (cntMap.get(num) > midBound) return num;
        }

        return -1;
    }
}