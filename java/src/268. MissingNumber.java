class Solution {
    public int missingNumber(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int i : nums) numSet.add(i);

        for (int i = 0; i < nums.length+1; i++) {
            if (!numSet.contains(i)) return i;
        }

        return 0;
    }
}