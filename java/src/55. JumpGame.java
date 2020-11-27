class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        if (nums == null || n == 0) return true;

        int maxIdx = 0;
        for (int i = 0; i < n; i++) {
            if (i > maxIdx) return false;
            
            maxIdx = Math.max(maxIdx, i + nums[i]);
            if (maxIdx >= n-1) return true;
        }

        return false;
    }
}