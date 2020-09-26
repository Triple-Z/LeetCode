class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int ans = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            int tempSum = nums[i];
            for (int j = i; j < n; j++) {
                if (j != i) tempSum += nums[j];
                ans = Math.max(ans, tempSum);
            }
        }

        return ans;
    }
}